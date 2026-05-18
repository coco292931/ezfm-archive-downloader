# EZFM-archive-downloader

EZFM / Hit FM 历史节目（点播回听）下载器

> **项目来源**：原为云听（YunTing）历史节目下载器，现已全面切换到 EZFM API（aezfm.meldingcloud.com），
> 绕开云听的签名鉴权，直接通过 `/program/historyList` 接口获取 Hit FM 各节目的历史回放数据。

## 说明

此项目是为了纪念Hit FM而生，也同样为了纪念那些离我们而去的声音

这个我从小学就开始听，陪伴我近9年的电台，在25年12月23日零时，永久沉寂了。。

不能说有多伤感，因为时代就是如此发展，电台终将会淡出人们的视野，

只是这次，恰好轮到887而已。



在这曲终人散之时，趁着云听尚存有Hit FM的回放，故写这样一个下载器，保存下来曾经的回忆

## 原理

通过root安卓抓包ezfm APP获得API接口

### 核心 API

**搜索接口**：`POST /program/search?programName={name}`  
返回该节目在各天的历史记录（包含 `programId` = 小节目 ID，`source` = 音频链接）。

**历史节目接口**：`POST /program/historyList?programId={大节目ID}&category=5&page={页号}`  
通过「大节目ID」分页获取该节目的全部历史回放数据，无需签名。

返回数据示例（省略非必要部分）：

```json
{
    "data": [
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/...mp3",
            "title": "Big Drive Home",
            "showDate": "2021-12-30",
            "duration": "03:00:00",
            "time": "16:00 - 19:00",
            "picurl": "https://radio-res.cgtn.com/...jpg",
            "programId": 2699849
        }
    ],
    "totalSize": 359,
    "totalPage": 18,
    "status": "1"
}
```

其中 `mediaUrl` 是音频下载链接，`picurl` 是节目封面图。

### 大节目 ID 对照

| 大节目 ID | 节目名称        |
|--------|-----------------|
| **431** | Big Drive Home   |
| **432** | Lazy Afternoon   |
| **433** | At Work Network  |
| **434** | Hit Morning Show |
| **435** | Morning Hits     |
| **436** | HitFM Dance      |
| **437** | New Music Express |

程序会依次遍历配置中的大节目 ID，通过 `historyList` 接口获取全部历史记录，然后按日期筛选出当天的节目进行下载。

## 功能与使用说明

目前提供了命令行与图形化（GUI）两套操作逻辑：

### 1. 命令行使用

```bash
# 单日下载（默认下载全部7个大节目的当天回放）
python downloader.py -d "21-12-31"

# 指定部分节目ID下载
python downloader.py -d "21-12-31" --program-ids "431,433,435"

# 多连日下载（跨度下载），并在每天中间延迟3秒
python downloader.py -d "20-09-01 to 21-12-31" --delay 3

# 不下载封面图片，同时指定输出目录为 my_radio_folder
python downloader.py -d "21-12-31" -o "my_radio_folder" --no-images

# 仅下载节目名匹配正则的节目，并用模板自定义输出路径/文件名
python downloader.py -d "21-12-31" --name-regex "Music|Morning" --filename-template "{date}\\{id}_{name_en}"

# 扫描所有大节目的全部历史日期并下载（全量模式）
python downloader.py --all
```

**所有支持的命令行参数：**

- `-h`, `--help` : 显示帮助信息。
- `-d DATE`, `--date DATE` : 指定单独日期 (如 `'21-12-31'`) 或日期范围 (如 `'20-09-01 to 21-12-31'`)。
- `-o OUTDIR`, `--outdir OUTDIR` : 下载的基础输出目录，默认为 `downloads`。
- `--no-images` : 阻止下载节目封面图片。
- `--delay DELAY` : 当执行多日持续下载时，请求日期间隔的睡眠时间(秒)，默认 `1.5`。
- `--name-regex NAME_REGEX` : 节目名正则筛选，仅下载匹配的节目（默认空，即不过滤）。
- `--filename-template FILENAME_TEMPLATE` : 自定义输出模板（默认 `{date}\\{name}`，支持 `{id}` `{name}` `{date}` `{name_ch}` `{name_en}` `{start_time}` `{end_time}` `{program_id}` `{parent_id}` `{parent_name}`）。
- `--program-ids PROGRAM_IDS` : 大节目ID，逗号分隔（默认全部，即 `431,432,433,434,435,436,437`）。
- `--all` : 扫描所有大节目的全部历史天数并下载（全量模式）。

说明：Windows 文件系统不允许 `:` `*` `?` 等字符，模板渲染后若包含这些字符，程序会自动转换为对应全角字符以保证可落盘。

高级配置（仅 `config.json`，不在 UI 暴露）：

- `max_rate_kbps`：下载限速（单位 KB/s）。`0` 表示不限速。

### 2. GUI 界面操作 (推荐)

直接运行 `python gui.py` 唤出界面。
**核心特性：**

- **可视化参数调整**：在界面输入日期范围（支持单日或多日）、节目ID（逗号分隔），更改保存目录、控制请求延迟，并支持节目名正则筛选和文件名模板（含自定义子目录）。相关的配置会自动保存到同目录下的 `config.json` 内作为默认预设。
- **模板预览区**：下载页新增"文件名模板预览"，固定以 `Morning Call 音乐叫早` 作为示例，实时展示模板渲染后的完整输出路径。
- **自定义下载项**：可以选择是否连带下载音频的封面图资源。
- **防止重复与元数据映射**：图片只下载一次（以 `downloaded_images.txt` 缓存），并且按对应节目的名字被重命名，源链接信息保存在 `images_info.txt` 中。下载目录会以日期按规则分类，并在文件夹内生成当天的抓取记录报告 `YYYY-MM-DD_program_info.txt`，包含实际下载的高/低音质标识。
- **二段安全中断保护 (防烂尾机制)**：
  - 下载过程所有的文件采用 `.part` 缓存形式写入；连接意外中断或主动停用绝不产生报废无发播放的文件。
  - **暂停/恢复**：随时中断/恢复主下载线程与转换线程。
  - **软停止**：结束当前文件后自动取消随后的全部任务队列，包含转换队列的安全平滑退出。
  - **强行停止**：即便正在执行途中，立刻截断释放资源，并彻底清理残断文件与子进程。
- **配置持久化防御**：退出时系统会自动比对参数差异并防错弹窗提示，避免丢失辛苦调好的配置。所有诸如路径偏好均为干净相对路径标准（如 `"downloads"`）存放于 `config.json`，方便跨设备携带。

## 自动化后处理 (格式转换管线)

虽然 m4a 已经比较高效，但是如果全部按高码率保存节目，对储存依然是一笔不小的开销。
通过指定本地 FFmpeg（内置环境检测），图形界面原生支持了**异步多线程自动转换管线**功能：

1. **并行解耦，边下边压**：将下载和转换彻底分作两条完全独立的任务线运作，并通过动态队列衔接。当下载完成某集后，系统将其立即投喂给后处理队列进行降码/转码操作，而下载线程刻不容缓并发拉取下一集，双轨齐发，大幅度缩减耗时！双日志窗（下载与FFmpeg）能实时观测交响乐般的同步执行态。
2. **丰富的转码规格参数**：
   - 支持向 `opus`, `mp3`, `aac`, `m4a` 目标重混流并细控采样率（防 Opus 规范等报错）、固定压缩码率及调用 CPU 线程数。
   - 提供 “跳过现有 / 仅覆盖 0kb 残除 / 全量覆盖” 的3态安全覆写保护。
   - 自由设定独立输出文件夹，也可原地安全覆盖并搭配【转换成功后删除原文件】一键式瘦身。
3. **封面图自动反嵌**：能够监测源同名或源下载图片，并运用 ffmpeg 将其作为【专辑封面素材】反向无损硬写入最终的音频内部（**注：Opus 格式使用原生的 FFmpeg 无法直接嵌入图片流，如果你需要为 Opus 音频嵌入封面，可见下方进阶替代方案**）。
4. **批处理人工干预排队**：系统更支持扫描单日或全集目录寻找遗漏文件，预先生成批处理终端命令清单；用户甚至可在命令编辑区自由增删改查单条命令执行。

#### 📖 进阶：如何为 Opus 封装格式嵌入封面？

目前直接通过 `FFmpeg` 转码为 Opus/Ogg 容器时，因底层容器不支持将图片作为独立视频流打包，直接写入会报错退出。如果您**必须**为 `.opus` / `.ogg` 文件附带封面，建议采用以下两种常用替代方案进行二次处理：

* **方案A：使用 Python 的 `mutagen` 库（推荐）**
  这是最纯净的办法。先通过 FFmpeg 将音频转码为您需要的 `.opus`（不在 ffmpeg 内拼接图片），接着编写一个小脚本，引入 `mutagen` 库。读取事先备好的封面图片并转化为 Base64 编码，最终作为 `METADATA_BLOCK_PICTURE` 这个特定的 Vorbis Comment 标签无损硬写到 `.opus` 之中。
* **方案B：使用官方的 `opusenc` 命令行工具**
  不再直接令 FFmpeg 压缩 opus，而是让其剥离图片纯粹导出无损的 `.wav` 临时音频流。随后调用 Xiph 官方维护的命令行工具，通过 `opusenc --picture cover.jpg input.wav output.opus`，一键令其在编码音频的同时自动妥善完成 Base64 处理封面并合成。

## 大节目 ID 对照表

EZFM Hit FM 各节目对应的 `大节目ID`：

| 大节目 ID | 节目名称            |
|:--------|:-----------------|
| **431** | Big Drive Home   |
| **432** | Lazy Afternoon   |
| **433** | At Work Network  |
| **434** | Hit Morning Show |
| **435** | Morning Hits     |
| **436** | HitFM Dance      |
| **437** | New Music Express |

## 维护者快速入口（供后续修改）

为了便于后续接手，本项目可按下面的分层理解：

- `downloader.py`：负责接口签名、节目列表请求、音频/图片下载与落盘。
- `converter.py`：只负责 FFmpeg 检测和命令拼装，不直接执行子进程。
- `gui.py`：负责 UI、状态机（暂停/软停/强停）、任务调度与下载/转码串联。

核心调用链如下：

1. **数据获取**：`fetch_all_history(program_id)` → 自动翻页获取某大节目的全部历史记录。
2. **按天下载**：`download_by_date(date_str, program_ids)` → 遍历大节目ID，筛选当天的节目下载。
3. **全量下载**：`download_all_programs()` → 先获取所有大节目的全部历史，按日期归类后逐天下载。
4. GUI 启动下载：`start_download_thread -> run_download -> download_by_date`。
5. 单文件下载完成后，`downloader.py` 通过 `post_process_cb` 回调通知 GUI。
6. GUI 侧生成 FFmpeg 命令并执行（自动队列或手动批处理）。

后续改动时，建议优先关注这些“联动点”：

- 若修改 `download_by_date(...)` 参数：同步调整 `gui.py` 的调用位置与 README 参数说明。
- 若修改 `build_ffmpeg_cmd(...)` 参数：同步调整 GUI 命令生成、配置读写字段。
- 若新增配置项：同步更新 GUI 变量初始化、`load_config/save_config`、`config_example.json`、README。

推荐最小自检：

- `python -m py_compile gui.py downloader.py converter.py`
- `python gui.py`
- `python downloader.py --help`

### GitHub Actions 自动打包（Windows/macOS/Linux）

仓库已提供工作流文件：`.github/workflows/build-multi-platform.yml`

触发方式：

1. 手动触发：
  - 打开 GitHub 仓库的 Actions 页面。
  - 选择 `Build Multi-Platform Releases`。
  - 点击 `Run workflow`，输入版本号（如 `1.0.0`）。
  - 工作流会自动构建三平台二进制，并创建/更新对应版本的 GitHub Release。

2. 发布触发（推荐）：
  - 推送符合 `v*` 规则的 tag（如 `v1.0.1`）。
  - 工作流会自动构建三平台二进制，并自动创建 GitHub Release，上传附件。
  - 每个平台会同时生成 GUI 版与 CLI 版（`downloader.py`）。

发布附件命名规则：

- `ezfm-archive-downloader_windows_V1.0.0.exe`
- `ezfm-archive-downloader_linux_V1.0.0.tar.gz`
- `ezfm-archive-downloader_macos_V1.0.0.tar.gz`
- `ezfm-archive-downloader_windows_V1.0.0_CLI.exe`
- `ezfm-archive-downloader_linux_V1.0.0_CLI.tar.gz`
- `ezfm-archive-downloader_macos_V1.0.0_CLI.tar.gz`

示例命令：

```bash
git tag v1.0.1
git push origin v1.0.1
```

注意：

- 若仓库未允许工作流写入 Release，请到仓库 Settings -> Actions -> General，将 Workflow permissions 设为 `Read and write permissions`。
- 当前仅 Windows 使用 `vtfts-knkbe-001.ico` 图标；macOS 如需图标请准备 `.icns` 并在工作流里单独加参数。

## 注意事项

EZFM API 目前没有限速和封禁策略，但保险起见，使用时仍需注意流量。

转码必然会导致音质损失，加上原音频也已经经过一层压缩，想保存留档的朋友请自行斟酌是否转换，并设定好参数，因转换导致的损失作者概不负责。

本工具仅供学习使用，请勿用作非法用途