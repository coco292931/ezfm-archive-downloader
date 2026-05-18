import requests
import os
import json
from datetime import datetime, timedelta
import time
import hashlib
import re
from urllib.parse import urlparse

# ============================================================
# EZFM API 配置
# ============================================================
API_BASE = "https://aezfm.meldingcloud.com"

# 大节目 ID 列表（API 不提供枚举接口，需保持此已知集合）
DEFAULT_PROGRAM_IDS = ["431", "432", "433", "434", "435", "436", "437"]


def _get_program_name(pid, *, cache_dir=None):
    """从 API 第一条历史记录动态获取节目名，避免硬编码。"""
    try:
        d = fetch_history_list(str(pid), 1, cache_dir=cache_dir, cache_ttl_seconds=API_CACHE_TTL_SECONDS)
        if d and isinstance(d, dict) and d.get("data"):
            items = d["data"]
            if isinstance(items, list) and items:
                title = items[0].get("title") or items[0].get("programTitle") or ""
                if title:
                    return title.strip()
    except Exception:
        pass
    return str(pid)

# historyList 参数常量
HISTORY_CATEGORY = "5"
HISTORY_PAGE_SIZE = 20

# ============================================================
# API 缓存/降频（降低访问频率，避免频繁打 EZFM）
# ============================================================
# 默认缓存 6 小时；如希望更激进可调小。
API_CACHE_TTL_SECONDS = 6 * 60 * 60
# cache miss 时最小请求间隔（秒）
API_MIN_INTERVAL_SECONDS = 0.25

_MEM_HISTORY_CACHE = {}  # (program_id, page_num) -> (ts, data)
_LAST_API_TS = 0.0


def _normalize_to_ymd(date_text):
    """把日期统一成 YYYY-MM-DD；支持 YY-MM-DD / YYYY-MM-DD，失败返回空串。"""
    s = (date_text or "").strip()
    if not s:
        return ""
    for fmt in ("%Y-%m-%d", "%y-%m-%d"):
        try:
            return datetime.strptime(s, fmt).strftime("%Y-%m-%d")
        except ValueError:
            pass
    return ""


def _fmt_path(path_text):
    try:
        return os.path.normpath(str(path_text))
    except Exception:
        return str(path_text)


def _print_section(title, width=40):
    line = "=" * int(width)
    print(line)
    print(str(title).strip())
    print(line)


def _ensure_cache_dir(cache_dir):
    d = cache_dir or os.path.join(os.path.dirname(__file__), ".api_cache")
    os.makedirs(d, exist_ok=True)
    return d


def _cache_file_path(cache_dir, program_id, page_num):
    safe_pid = re.sub(r"[^0-9A-Za-z_-]", "_", str(program_id))
    return os.path.join(cache_dir, f"historyList_{safe_pid}_p{int(page_num)}.json")


def _cache_get(cache_path, ttl_seconds):
    try:
        if not os.path.exists(cache_path):
            return None
        age = time.time() - os.path.getmtime(cache_path)
        if ttl_seconds is not None and ttl_seconds >= 0 and age > float(ttl_seconds):
            return None
        with open(cache_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def _cache_set(cache_path, data):
    try:
        tmp = cache_path + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False)
        os.replace(tmp, cache_path)
    except Exception:
        pass

def _load_downloaded_images(log_file):
    if not os.path.exists(log_file):
        return set()
    with open(log_file, 'r', encoding='utf-8') as f:
        return set(line.strip() for line in f if line.strip())

def _save_downloaded_image(log_file, url):
    with open(log_file, 'a', encoding='utf-8') as f:
        f.write(f"{url}\n")

def download_image(url, img_dir, headers, downloaded_images_log, images_info_log, safe_program_name, suffix=""):
    if not url:
        return ""
    
    images_cache = _load_downloaded_images(downloaded_images_log)
        
    try:
        parsed_url = urlparse(url)
        original_name = os.path.basename(parsed_url.path)
        if not original_name:
            original_name = hashlib.md5(url.encode('utf-8')).hexdigest() + ".jpg"

        _, ext = os.path.splitext(original_name)
        if not ext:
            ext = ".jpg"

        new_img_name = f"{safe_program_name}{suffix}{ext}"
        img_path = os.path.join(img_dir, new_img_name)
        
        is_cached = url in images_cache
        if os.path.exists(img_path) or is_cached:
            if not is_cached:
                _save_downloaded_image(downloaded_images_log, url)
            return ""
            
        print(f"正在下载图片: {url} -> '{_fmt_path(img_path)}'")
        img_response = requests.get(url, headers={'User-Agent': headers.get('user-agent', '')}, stream=True)
        img_response.raise_for_status()
        with open(img_path, 'wb') as f:
            for chunk in img_response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        _save_downloaded_image(downloaded_images_log, url)

        with open(images_info_log, 'a', encoding='utf-8') as info_f:
            info_f.write(f"本地命名: {new_img_name}\n")
            info_f.write(f"原始文件: {original_name}\n")
            info_f.write(f"来源地址: {url}\n")
            info_f.write("-" * 40 + "\n")

        return f"（新保存：{new_img_name}）"
    except Exception as e:
        print(f"下载图片失败 {url}: {e}")
        return "（下载失败）"

class _TokenBucketLimiter:
    def __init__(self, rate_kbps):
        self.rate_bps = max(float(rate_kbps), 0.0) * 1024.0
        self.capacity = max(self.rate_bps * 0.5, 16 * 1024)
        self.tokens = self.capacity
        self.last_ts = time.monotonic()

    def consume(self, size_bytes):
        if self.rate_bps <= 0:
            return
        need = float(size_bytes)
        while True:
            now = time.monotonic()
            elapsed = max(0.0, now - self.last_ts)
            self.last_ts = now
            self.tokens = min(self.capacity, self.tokens + elapsed * self.rate_bps)
            if self.tokens >= need:
                self.tokens -= need
                return
            wait_s = (need - self.tokens) / self.rate_bps
            time.sleep(min(max(wait_s, 0.001), 0.2))

class _SafeFormatDict(dict):
    def __missing__(self, key):
        return "{" + key + "}"

def _sanitize_component_for_path(value):
    if value is None:
        return ""
    text = str(value)
    translate_map = {
        "<": "＜", ">": "＞", ":": "：", '\"': "＂", "/": "／", "\\": "＼", "|": "｜", "?": "？", "*": "＊",
    }
    cleaned = "".join(translate_map.get(ch, ch) for ch in text).strip()
    cleaned = cleaned.rstrip(". ")
    return cleaned or "_"

def _split_program_name(name):
    raw = (name or "").strip()
    pattern = r"^(?P<en>[A-Za-z0-9][A-Za-z0-9&().,'!?:/\-\s]*?)\s+(?P<ch>[\u3400-\u9fff].*)$"
    m = re.match(pattern, raw)
    if m:
        return m.group("en").strip(), m.group("ch").strip()
    if re.search(r"[\u3400-\u9fff]", raw):
        return "", raw
    return raw, ""

def _render_filename_template(template, values):
    tpl = (template or "").strip() or r"{date}\{name}"
    return tpl.format_map(_SafeFormatDict(values))

def _extract_audio_extension(download_url):
    ext = os.path.splitext(urlparse(download_url).path)[1].lower()
    return ext if ext else ".m4a"

def _build_output_file_path(base_downloads_dir, template_rendered, download_url, fallback_date, fallback_name):
    rel = (template_rendered or "").strip().replace("/", os.sep).replace("\\", os.sep)
    if not rel:
        rel = os.path.join(fallback_date, fallback_name)

    if os.path.isabs(rel):
        drive, tail = os.path.splitdrive(rel)
        parts = [p for p in tail.split(os.sep) if p not in ("", ".", "..")]
        safe_parts = [_sanitize_component_for_path(p) for p in parts]
        if drive:
            path_no_ext = os.path.join(drive + os.sep, *safe_parts)
        else:
            path_no_ext = os.path.join(os.sep, *safe_parts)
    else:
        parts = [p for p in rel.split(os.sep) if p not in ("", ".", "..")]
        safe_parts = [_sanitize_component_for_path(p) for p in parts]
        if not safe_parts:
            safe_parts = [_sanitize_component_for_path(fallback_date), _sanitize_component_for_path(fallback_name)]
        path_no_ext = os.path.join(base_downloads_dir, *safe_parts)

    return path_no_ext + _extract_audio_extension(download_url)

def fetch_history_list(program_id, page_num=1, *, cache_dir=None, cache_ttl_seconds=API_CACHE_TTL_SECONDS, min_interval_seconds=API_MIN_INTERVAL_SECONDS):
    """获取 EZFM historyList 单页。

    - 默认启用磁盘+内存缓存（TTL），减少重复访问。
    - cache miss 时做最小请求间隔，进一步降频。
    """
    global _LAST_API_TS

    key = (str(program_id), int(page_num))
    now = time.time()
    mem_hit = _MEM_HISTORY_CACHE.get(key)
    if mem_hit:
        ts, cached = mem_hit
        if cache_ttl_seconds is None or cache_ttl_seconds < 0 or (now - ts) <= float(cache_ttl_seconds):
            return cached

    cache_dir = _ensure_cache_dir(cache_dir)
    cache_path = _cache_file_path(cache_dir, program_id, page_num)
    disk_hit = _cache_get(cache_path, cache_ttl_seconds)
    if disk_hit is not None:
        _MEM_HISTORY_CACHE[key] = (now, disk_hit)
        return disk_hit

    # cache miss：做最小请求间隔
    wait_s = float(min_interval_seconds or 0) - (now - float(_LAST_API_TS or 0.0))
    if wait_s > 0:
        time.sleep(min(wait_s, 2.0))

    url = f"{API_BASE}/program/historyList"
    # 注意：该接口在一些环境下不接受 JSON body（会提示 category 为空）。
    # 使用 form（application/x-www-form-urlencoded）更稳。
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://aezfm.meldingcloud.com/",
        "Origin": "https://aezfm.meldingcloud.com",
    }
    payload = {
        "category": HISTORY_CATEGORY,
        "programId": str(program_id),
        "page": str(int(page_num)),
        "pageSize": str(int(HISTORY_PAGE_SIZE)),
    }

    try:
        resp = requests.post(url, data=payload, headers=headers, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        _LAST_API_TS = time.time()
        _MEM_HISTORY_CACHE[key] = (_LAST_API_TS, data)
        _cache_set(cache_path, data)
        return data
    except Exception as e:
        print(f"获取历史列表失败 (ID: {program_id}, Page: {page_num}): {e}")
        return None


def _write_info_line(base_downloads_dir, show_date_ymd, day_index, program_name, pname_with_pid, small_id, start_time, end_time, download_url, file_path):
    info_txt_path = os.path.join(base_downloads_dir, show_date_ymd, f"{show_date_ymd}_program_info.txt")
    try:
        os.makedirs(os.path.dirname(info_txt_path), exist_ok=True)
        first_write = not os.path.exists(info_txt_path)
        with open(info_txt_path, "a", encoding="utf-8") as f:
            if first_write:
                f.write(f"=== {show_date_ymd} EZFM 节目信息 ===\n\n")
            f.write(f"节目名称: {program_name}\n")
            f.write(f"节目序号: {day_index}\n")
            f.write(f"大节目ID: {pname_with_pid}\n")
            f.write(f"小节目ID: {small_id}\n")
            f.write(f"开始时间: {show_date_ymd} {start_time}:00\n")
            f.write(f"结束时间: {show_date_ymd} {end_time}:00\n")
            f.write(f"下载链接: {download_url}\n")
            f.write(f"输出路径: {_fmt_path(file_path)}\n")
            f.write("-" * 40 + "\n")
    except Exception as e:
        print(f"写入节目信息文件失败 {info_txt_path}: {e}")


def fetch_all_history(program_id, *, cache_dir=None, cache_ttl_seconds=API_CACHE_TTL_SECONDS):
    all_items = []
    page = 1
    while True:
        data = fetch_history_list(program_id, page, cache_dir=cache_dir, cache_ttl_seconds=cache_ttl_seconds)
        if not data:
            break

        # 兼容不同返回形态：有的用 status=1，有的用 code=200
        if not isinstance(data, dict) or str(data.get("status")) != "1":
            break

        raw_payload = data.get("data")
        payload = raw_payload

        # 有些返回会把 data 再 JSON 编码成字符串（如 '[]' 或 '{"items":...}'）
        if isinstance(payload, str):
            try:
                payload = json.loads(payload)
            except Exception:
                payload = None

        items = []
        total_page = 1

        # 形态 A：顶层 data 是 list，分页信息在顶层 totalPage
        if isinstance(payload, list):
            items = payload
            try:
                total_page = int(data.get("totalPage") or 1)
            except Exception:
                total_page = 1

        # 形态 B：data 是 dict，含 items/totalPage
        elif isinstance(payload, dict):
            items = payload.get("items") or []
            try:
                total_page = int(payload.get("totalPage") or data.get("totalPage") or 1)
            except Exception:
                total_page = 1

        if items:
            all_items.extend(items)

        if page >= total_page or not items:
            break
        page += 1
    return all_items


def _parse_history_page_items(data):
    """把 historyList 的响应解析成 (items, total_page, total_size)。"""
    if not data or not isinstance(data, dict):
        return [], 1, 0
    if str(data.get("status")) != "1":
        return [], 1, 0

    raw_payload = data.get("data")
    payload = raw_payload
    if isinstance(payload, str):
        try:
            payload = json.loads(payload)
        except Exception:
            payload = None

    items = []
    total_page = 1
    if isinstance(payload, list):
        items = payload
        try:
            total_page = int(data.get("totalPage") or 1)
        except Exception:
            total_page = 1
    elif isinstance(payload, dict):
        items = payload.get("items") or []
        try:
            total_page = int(payload.get("totalPage") or data.get("totalPage") or 1)
        except Exception:
            total_page = 1

    try:
        total_size = int(data.get("totalSize") or 0)
    except Exception:
        total_size = 0

    return items or [], max(int(total_page or 1), 1), max(int(total_size or 0), 0)


def _get_history_summary(program_id, *, cache_dir=None, cache_ttl_seconds=API_CACHE_TTL_SECONDS):
    """拿到 (total_page, total_size, newest_date, oldest_date)。"""
    d1 = fetch_history_list(program_id, 1, cache_dir=cache_dir, cache_ttl_seconds=cache_ttl_seconds)
    items1, total_page, total_size = _parse_history_page_items(d1)
    newest = ""
    if items1:
        newest = _normalize_to_ymd((items1[0].get("showDate") or "").strip())

    oldest = ""
    if total_page <= 1:
        if items1:
            oldest = _normalize_to_ymd((items1[-1].get("showDate") or "").strip())
        return total_page, total_size, newest, oldest

    dlast = fetch_history_list(program_id, total_page, cache_dir=cache_dir, cache_ttl_seconds=cache_ttl_seconds)
    items_last, _, _ = _parse_history_page_items(dlast)
    if items_last:
        oldest = _normalize_to_ymd((items_last[-1].get("showDate") or "").strip())
    return total_page, total_size, newest, oldest


def _iter_history_items(program_id, *, cache_dir=None, cache_ttl_seconds=API_CACHE_TTL_SECONDS, oldest_first=False):
    """按页迭代历史条目。

    - 默认 newest->oldest（页 1..N，页内保持原顺序）。
    - oldest_first=True：oldest->newest（页 N..1，页内反转）。
    """
    d1 = fetch_history_list(program_id, 1, cache_dir=cache_dir, cache_ttl_seconds=cache_ttl_seconds)
    items1, total_page, _ = _parse_history_page_items(d1)
    if total_page <= 1:
        items = list(items1 or [])
        if oldest_first:
            items.reverse()
        for it in items:
            yield it
        return

    pages = range(total_page, 0, -1) if oldest_first else range(1, total_page + 1)
    for page in pages:
        if page == 1:
            data = d1
        else:
            data = fetch_history_list(program_id, page, cache_dir=cache_dir, cache_ttl_seconds=cache_ttl_seconds)
        items, _, _ = _parse_history_page_items(data)
        if not items:
            continue
        if oldest_first:
            items = list(items)
            items.reverse()
        for it in items:
            yield it


def _download_for_span(start_ymd, end_ymd, *, program_ids, base_downloads_dir, download_imgs, state_checker, post_process_cb,
                       download_progress_cb, name_pattern, filename_template, max_rate_kbps, oldest_first, delay_seconds=0):
    """两阶段：先摘要（一次性输出所有节目信息）→ 再实际下载。"""
    api_cache_dir = os.path.join(base_downloads_dir, ".api_cache")

    # 归一化边界：内部始终 start <= end，方向由 oldest_first 控制
    if start_ymd > end_ymd:
        start_ymd, end_ymd = end_ymd, start_ymd

    # ---- 阶段 1：摘要（不下载，不走 state_checker/limiter/images） ----
    hit_labels = []
    for pid in program_ids:
        pname = _get_program_name(pid, cache_dir=api_cache_dir)
        label = f"{pid} ({pname})"
        total_page, total_size, newest, oldest = _get_history_summary(pid, cache_dir=api_cache_dir)
        cover = ""
        if oldest and newest:
            cover = f"{oldest} ~ {newest}"
        elif newest:
            cover = newest
        elif oldest:
            cover = oldest
        else:
            cover = "未知"

        matched_count = 0
        for item in _iter_history_items(pid, cache_dir=api_cache_dir, oldest_first=oldest_first):
            show_date_ymd = _normalize_to_ymd((item.get("showDate") or "").strip())
            if not show_date_ymd:
                continue
            if oldest_first:
                if show_date_ymd > end_ymd:
                    break
                if show_date_ymd < start_ymd:
                    continue
            else:
                if show_date_ymd < start_ymd:
                    break
                if show_date_ymd > end_ymd:
                    continue
            program_name = (item.get("title") or item.get("programName") or item.get("name") or "unknown").strip() or "unknown"
            if name_pattern and not name_pattern.search(program_name):
                continue
            download_url = item.get("mediaUrl") or item.get("playUrl") or item.get("backUrl")
            if not download_url:
                continue
            matched_count += 1

        if matched_count == 0:
            print(f"{label}无可下载条目,跳过")
        else:
            print(f"{label}命中 {matched_count} 条（{cover}）")
            hit_labels.append(pid)

    if not hit_labels:
        return

    print("\n----- 节目列表获取完成，开始下载 -----\n")

    # ---- 阶段 2：实际下载 ----
    limiter = _TokenBucketLimiter(max_rate_kbps) if float(max_rate_kbps or 0) > 0 else None
    images_dir = os.path.join(base_downloads_dir, "images")
    downloaded_images_log = os.path.join(base_downloads_dir, "downloaded_images.txt")
    images_info_log = os.path.join(images_dir, "images_info.txt")
    for d in [base_downloads_dir, images_dir]:
        if not os.path.exists(d):
            os.makedirs(d)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    # 先把所有命中条目按日期分组
    _date_items = {}  # show_date_ymd -> [(program_name, download_url, pid, item, ...)]
    for pid in hit_labels:
        for item in _iter_history_items(pid, cache_dir=api_cache_dir, oldest_first=oldest_first):
            show_date_raw = (item.get("showDate") or "").strip()
            show_date_ymd = _normalize_to_ymd(show_date_raw) or show_date_raw
            if not show_date_ymd:
                continue
            if oldest_first:
                if show_date_ymd > end_ymd:
                    break
                if show_date_ymd < start_ymd:
                    continue
            else:
                if show_date_ymd < start_ymd:
                    break
                if show_date_ymd > end_ymd:
                    continue
            program_name = (item.get("title") or item.get("programName") or item.get("name") or "unknown").strip() or "unknown"
            if name_pattern and not name_pattern.search(program_name):
                continue
            download_url = item.get("mediaUrl") or item.get("playUrl") or item.get("backUrl")
            if not download_url:
                continue
            _date_items.setdefault(show_date_ymd, []).append((pid, item, program_name, download_url, show_date_ymd, show_date_raw))

    # 按日期顺序遍历（oldest_first 决定日期本身的正反）
    sorted_dates = sorted(_date_items.keys(), reverse=not oldest_first)
    _last_file_date = None
    for show_date_ymd in sorted_dates:
        if _last_file_date is not None and float(delay_seconds or 0) > 0:
            for _ in range(int(float(delay_seconds) * 10)):
                if state_checker:
                    state_checker(is_chunk=False)
                time.sleep(0.1)
        _last_file_date = show_date_ymd
        _day_index = 0  # 每日序号归零

        for pid, item, program_name, download_url, show_date_ymd, show_date_raw in _date_items[show_date_ymd]:
            if state_checker:
                state_checker(is_chunk=False)

            name_en, name_ch = _split_program_name(program_name)
            format_values = {
                "id": str(pid),
                "name": _sanitize_component_for_path(program_name),
                "date": _sanitize_component_for_path(show_date_ymd),
                "name_ch": _sanitize_component_for_path(name_ch),
                "name_en": _sanitize_component_for_path(name_en),
                "bitrate": "Standard",
                "start_time": _sanitize_component_for_path((item.get("time", "") or "").split("-")[0].strip()),
                "end_time": _sanitize_component_for_path((item.get("time", "") or "").split("-")[1].strip() if "-" in (item.get("time", "") or "") else ""),
            }

            template_rendered = _render_filename_template(filename_template, format_values)
            file_path = _build_output_file_path(
                base_downloads_dir,
                template_rendered,
                download_url,
                show_date_ymd or start_ymd or show_date_raw,
                program_name,
            )
            os.makedirs(os.path.dirname(file_path), exist_ok=True)

            img_url = (item.get("picurl") or item.get("picurl1") or item.get("programUrl") or item.get("imageUrl") or item.get("imageLongUrl") or "")
            if download_imgs and img_url:
                img_base = os.path.splitext(os.path.basename(file_path))[0]
                download_image(img_url, images_dir, headers, downloaded_images_log, images_info_log, img_base)

            if os.path.exists(file_path):
                print(f"已存在，跳过下载: {_fmt_path(file_path)}")
                _day_index += 1
                #pname_with_pid = f"{pid} ({_get_program_name(pid, cache_dir=api_cache_dir)})"
                #small_id = str(item.get("programId") or "")
                #start_time = (item.get("time", "") or "").split("-")[0].strip()
                #end_time = (item.get("time", "") or "").split("-")[1].strip() if "-" in (item.get("time", "") or "") else ""
                #_write_info_line(base_downloads_dir, show_date_ymd, _day_index, program_name, pid, small_id, start_time, end_time, download_url, file_path)
                if post_process_cb:
                    post_process_cb(os.path.splitext(os.path.basename(file_path))[0], file_path, show_date_ymd or show_date_raw)
                continue

            print(f"正在下载 {program_name} 到 {_fmt_path(file_path)}...")
            part_path = file_path + ".part"
            try:
                r = requests.get(download_url, headers=headers, stream=True, timeout=30)
                r.raise_for_status()
                with open(part_path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if state_checker:
                            state_checker(is_chunk=True)
                        if chunk:
                            if limiter:
                                limiter.consume(len(chunk))
                            if download_progress_cb:
                                download_progress_cb(len(chunk))
                            f.write(chunk)
                os.replace(part_path, file_path)
                _day_index += 1
                #pname_with_pid = f"{pid} ({_get_program_name(pid, cache_dir=api_cache_dir)})"
                small_id = str(item.get("programId") or "")
                start_time = (item.get("time", "") or "").split("-")[0].strip()
                end_time = (item.get("time", "") or "").split("-")[1].strip() if "-" in (item.get("time", "") or "") else ""
                _write_info_line(base_downloads_dir, show_date_ymd, _day_index, program_name, pid, small_id, start_time, end_time, download_url, file_path)
                print(f"{program_name} 下载完成。\n")
                if post_process_cb:
                    post_process_cb(os.path.splitext(os.path.basename(file_path))[0], file_path, show_date_ymd or show_date_raw)
            except Exception as e:
                if os.path.exists(part_path):
                    os.remove(part_path)
                if "StopDownloadException" in str(type(e)):
                    print("\n>>>> 任务安全切断: 操作取消. <<<<\n")
                    raise
                print(f"下载失败 {program_name}: {e}")

def download_by_date(date_str, program_ids=None, base_downloads_dir="downloads", download_imgs=True, state_checker=None, post_process_cb=None, download_progress_cb=None, name_filter_regex="", filename_template=r"{date}\{name}", fetch_all=False, max_rate_kbps=0, oldest_first=False, delay_seconds=0):
    if program_ids is None:
        program_ids = list(DEFAULT_PROGRAM_IDS)
    name_pattern = None
    if name_filter_regex and name_filter_regex.strip():
        try:
            name_pattern = re.compile(name_filter_regex)
        except re.error as e:
            print(f"正则表达式错误: {e}")
            return
    _print_section("启动自动化下载管线流")
    if fetch_all:
        api_cache_dir = os.path.join(base_downloads_dir, ".api_cache")
        hit_labels = []
        for pid in program_ids:
            if state_checker:
                state_checker(is_chunk=False)
            label = f"{pid} ({_get_program_name(pid, cache_dir=api_cache_dir)})"
            items = fetch_all_history(pid, cache_dir=api_cache_dir)
            if not items:
                print(f"{label}无可下载条目,跳过")
                continue
            newest = _normalize_to_ymd((items[0].get("showDate") or "").strip())
            oldest = _normalize_to_ymd((items[-1].get("showDate") or "").strip())
            cover = f"{oldest} ~ {newest}" if oldest and newest else (newest or oldest or "未知")
            print(f"{label}命中 {len(items)} 条（{cover}）")
            hit_labels.append(pid)
        if not hit_labels:
            print("\n---------- 下载转换完成 ----------")
            return
        limiter = _TokenBucketLimiter(max_rate_kbps) if float(max_rate_kbps or 0) > 0 else None
        images_dir = os.path.join(base_downloads_dir, "images")
        downloaded_images_log = os.path.join(base_downloads_dir, "downloaded_images.txt")
        images_info_log = os.path.join(images_dir, "images_info.txt")
        for d in [base_downloads_dir, images_dir]:
            if not os.path.exists(d):
                os.makedirs(d)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        for pid in hit_labels:
            items = fetch_all_history(pid, cache_dir=api_cache_dir)
            if not items:
                continue
            for item in items:
                if state_checker:
                    state_checker(is_chunk=False)
                show_date_ymd = _normalize_to_ymd((item.get("showDate") or "").strip())
                program_name = (item.get("title") or item.get("programName") or item.get("name") or "unknown").strip() or "unknown"
                if name_pattern and not name_pattern.search(program_name):
                    continue
                download_url = item.get("mediaUrl") or item.get("playUrl") or item.get("backUrl")
                if not download_url:
                    continue
                name_en, name_ch = _split_program_name(program_name)
                format_values = {
                    "id": str(pid), "name": _sanitize_component_for_path(program_name),
                    "date": _sanitize_component_for_path(show_date_ymd),
                    "name_ch": _sanitize_component_for_path(name_ch), "name_en": _sanitize_component_for_path(name_en),
                    "bitrate": "Standard",
                    "start_time": _sanitize_component_for_path((item.get("time", "") or "").split("-")[0].strip()),
                    "end_time": _sanitize_component_for_path((item.get("time", "") or "").split("-")[1].strip() if "-" in (item.get("time", "") or "") else ""),
                }
                template_rendered = _render_filename_template(filename_template, format_values)
                file_path = _build_output_file_path(base_downloads_dir, template_rendered, download_url, show_date_ymd or date_str, program_name)
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                if download_imgs:
                    img_url = (item.get("picurl") or item.get("picurl1") or item.get("programUrl") or item.get("imageUrl") or item.get("imageLongUrl") or "")
                    if img_url:
                        img_base = os.path.splitext(os.path.basename(file_path))[0]
                        download_image(img_url, images_dir, headers, downloaded_images_log, images_info_log, img_base)
                if os.path.exists(file_path):
                    if post_process_cb:
                        post_process_cb(os.path.splitext(os.path.basename(file_path))[0], file_path, show_date_ymd or date_str)
                    continue
                print(f"正在下载 {program_name} 到 {_fmt_path(file_path)}...")
                part_path = file_path + ".part"
                try:
                    r = requests.get(download_url, headers=headers, stream=True, timeout=30)
                    r.raise_for_status()
                    with open(part_path, "wb") as f:
                        for chunk in r.iter_content(chunk_size=8192):
                            if state_checker:
                                state_checker(is_chunk=True)
                            if chunk:
                                if limiter:
                                    limiter.consume(len(chunk))
                                if download_progress_cb:
                                    download_progress_cb(len(chunk))
                                f.write(chunk)
                    os.replace(part_path, file_path)
                    print(f"{program_name} 下载完成。\n")
                    if post_process_cb:
                        post_process_cb(os.path.splitext(os.path.basename(file_path))[0], file_path, show_date_ymd or date_str)
                except Exception as e:
                    if os.path.exists(part_path):
                        os.remove(part_path)
                    if "StopDownloadException" in str(type(e)):
                        print("\n>>>> 任务安全切断: 操作取消. <<<<\n")
                        raise
                    print(f"下载失败 {program_name}: {e}")
    else:
        target_date_ymd = _normalize_to_ymd(date_str)
        if not target_date_ymd:
            print(f"错误：日期格式不正确: {date_str}，请使用 'YY-MM-DD' 或 'YYYY-MM-DD'。")
            print("\n---------- 下载转换完成 ----------")
            return
        print(f"正在获取 {target_date_ymd} 的节目列表...")
        _download_for_span(
            target_date_ymd, target_date_ymd,
            program_ids=program_ids, base_downloads_dir=base_downloads_dir,
            download_imgs=download_imgs, state_checker=state_checker,
            post_process_cb=post_process_cb, download_progress_cb=download_progress_cb,
            name_pattern=name_pattern, filename_template=filename_template,
            max_rate_kbps=max_rate_kbps, oldest_first=oldest_first, delay_seconds=delay_seconds,
        )
    print("\n---------- 下载转换完成 ----------")

def download_all_programs(program_ids=None, base_downloads_dir="downloads", download_imgs=True, state_checker=None, post_process_cb=None, download_progress_cb=None, name_filter_regex="", filename_template=r"{date}\{name}", max_rate_kbps=0, delay_seconds=0):
    if program_ids is None:
        program_ids = list(DEFAULT_PROGRAM_IDS)
    
    download_by_date(
        date_str="", 
        program_ids=program_ids,
        base_downloads_dir=base_downloads_dir,
        download_imgs=download_imgs,
        state_checker=state_checker,
        post_process_cb=post_process_cb,
        download_progress_cb=download_progress_cb,
        name_filter_regex=name_filter_regex,
        filename_template=filename_template,
        fetch_all=True,
        max_rate_kbps=max_rate_kbps,
        delay_seconds=delay_seconds,
    )


def download_by_date_range(start_date_str, end_date_str, program_ids=None, base_downloads_dir="downloads", download_imgs=True, state_checker=None, post_process_cb=None,
                           download_progress_cb=None, name_filter_regex="", filename_template=r"{date}\{name}", max_rate_kbps=0, delay_seconds=0):
    if program_ids is None:
        program_ids = list(DEFAULT_PROGRAM_IDS)
    name_pattern = None
    if name_filter_regex and name_filter_regex.strip():
        try:
            name_pattern = re.compile(name_filter_regex)
        except re.error as e:
            print(f"正则表达式错误: {e}")
            return
    start_ymd = _normalize_to_ymd(start_date_str)
    end_ymd = _normalize_to_ymd(end_date_str)
    if not start_ymd or not end_ymd:
        print(f"错误：日期格式不正确: {start_date_str} ~ {end_date_str}，请使用 'YY-MM-DD' 或 'YYYY-MM-DD'。")
        return
    # 原样保持用户的顺序：start→end
    # 如果 end<start，用户期望从新到旧，oldest_first=False（默认新→旧）
    # 如果 start<end，用户期望从旧到新，oldest_first=True
    if start_ymd > end_ymd:
        oldest_first = False
    else:
        oldest_first = True
    _print_section("启动自动化下载管线流")
    order_text = "旧→新" if oldest_first else "新→旧"
    print(f"下载日期范围: {start_ymd} ~ {end_ymd}（{order_text}）")
    _download_for_span(
        start_ymd, end_ymd,
        program_ids=program_ids, base_downloads_dir=base_downloads_dir,
        download_imgs=download_imgs, state_checker=state_checker,
        post_process_cb=post_process_cb, download_progress_cb=download_progress_cb,
        name_pattern=name_pattern, filename_template=filename_template,
        max_rate_kbps=max_rate_kbps, oldest_first=oldest_first, delay_seconds=delay_seconds,
    )
    print("\n---------- 下载转换完成 ----------")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="EZFM 归档下载器")
    parser.add_argument("-d", "--date", help="指定日期 (YY-MM-DD)", default=datetime.now().strftime("%y-%m-%d"))
    parser.add_argument("-p", "--program-ids", help="节目 ID，逗号分隔", default=",".join(DEFAULT_PROGRAM_IDS))
    parser.add_argument("-o", "--outdir", help="输出目录", default="downloads")
    parser.add_argument("--all", help="下载该节目所有历史记录", action="store_true")
    parser.add_argument("--no-images", help="不下载封面图", action="store_true")
    parser.add_argument("--name-regex", help="节目名正则过滤", default="")
    parser.add_argument("--filename-template", help="输出文件名模板", default=r"{date}\{name}")
    parser.add_argument("--rate", help="限速 (KB/s)", type=int, default=0)
    parser.add_argument("--delay", help="每日之间间隔 (秒)", type=float, default=0)

    args = parser.parse_args()
    p_ids = [pid.strip() for pid in args.program_ids.split(",") if pid.strip()]
    
    if args.all:
        download_all_programs(
            program_ids=p_ids,
            base_downloads_dir=args.outdir,
            download_imgs=not args.no_images,
            name_filter_regex=args.name_regex,
            filename_template=args.filename_template,
            max_rate_kbps=args.rate,
            delay_seconds=float(args.delay or 0),
        )
    else:
        if " to " in args.date:
            start_s, end_s = args.date.split(" to ")
            download_by_date_range(
                start_s.strip(),
                end_s.strip(),
                program_ids=p_ids,
                base_downloads_dir=args.outdir,
                download_imgs=not args.no_images,
                name_filter_regex=args.name_regex,
                filename_template=args.filename_template,
                max_rate_kbps=args.rate,
                delay_seconds=float(args.delay or 0),
            )
        else:
            download_by_date(
                args.date,
                program_ids=p_ids,
                base_downloads_dir=args.outdir,
                download_imgs=not args.no_images,
                name_filter_regex=args.name_regex,
                filename_template=args.filename_template,
                max_rate_kbps=args.rate,
                delay_seconds=float(args.delay or 0),
            )
