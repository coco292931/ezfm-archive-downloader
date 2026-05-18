---
title: 默认模块
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
code_clipboard: true
highlight_theme: darkula
headingLevel: 2
generator: "@tarslib/widdershins v4.0.30"

---

# 默认模块

Base URLs: aezfm.meldingcloud.com

# Authentication

# hitfm

## POST 众多节目直播列表

POST /v3/live

### 请求参数

| 名称      | 位置    | 类型     | 必选  | 说明   |
| ------- | ----- | ------ | --- | ---- |
| session | query | string | 否   | none |

> 返回示例

> 200 Response

```json
{"data":[{"mediaUrl":"https://sk.cri.cn/am846.m3u8","programUrl":"https://radio-res.cgtn.com/image/2112/1639986367791.jpg","liveLinkUrl":"","id":22,"title":"CGTN Radio "},{"mediaUrl":"https://english-livetx.cgtn.com/hls/yypdyyctzb_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2210/1665880315954.jpg","liveLinkUrl":"","id":44,"title":"CGTN ENGLISH"},{"mediaUrl":"https://english-livetx.cgtn.com/hls/yypdjlctzb_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2101/1611302122849.jpg","liveLinkUrl":"","id":42,"title":"CGTN Documentary"},{"mediaUrl":"https://sk.cri.cn/887.m3u8","programUrl":"https://radio-res.cgtn.com/image/1907/1563347472411.jpg","liveLinkUrl":"","id":32,"title":"HIT FM"},{"mediaUrl":"https://sk.cri.cn/nhzs.m3u8","programUrl":"https://radio-res.cgtn.com/image/2009/1599459797746.jpg","liveLinkUrl":"","id":37,"title":"南海之声"},{"mediaUrl":"https://english-livetx.cgtn.com/hls/LSvexABhNipibK5KRuUkvHZ7220802LSTeze9o8tdFXMHsb1VosgoT220802_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2112/1640518624484.png","liveLinkUrl":"","id":41,"title":"CGTN Русский"},{"mediaUrl":"https://english-livetx.cgtn.com/hls/LSveq57bErWLinBnxosqjisZ220802LSTefTAS9zc9mpU08y3np9TH220802_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2101/1611302025524.jpg","liveLinkUrl":"","id":40,"title":"CGTN العربية"},{"mediaUrl":"https://sk.cri.cn/frenchafrica.m3u8","programUrl":"https://radio-res.cgtn.com/image/2303/1679647326705.png","liveLinkUrl":"","id":43,"title":"CGTN Radio Français"},{"mediaUrl":"https://english-livetx.cgtn.com/hls/LSveOGBaBw41Ea7ukkVAUdKQ220802LSTexu6xAuFH8VZNBLE1ZNEa220802_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2112/1640551167742.jpg","liveLinkUrl":"","id":38,"title":"CGTN Español"},{"mediaUrl":"https://english-livetx.cgtn.com/hls/LSvev95OuFZtKLc6CeKEFYXj220802LSTeV6PO0Ut9r71Uq3k5goCA220802_sd.m3u8","programUrl":"https://radio-res.cgtn.com/image/2112/1640551252956.jpg","liveLinkUrl":"","id":39,"title":"CGTN Français"}],"message":"接口请求成功。","status":"1"}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明   | 数据模型   |
| --- | ------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline |

### 返回数据结构

状态码 **200**

| 名称             | 类型       | 必选   | 约束   | 中文名  | 说明   |
| -------------- | -------- | ---- | ---- | ---- | ---- |
| » data         | [object] | true | none |      | none |
| »» mediaUrl    | string   | true | none | 直播地址 | none |
| »» programUrl  | string   | true | none | 图片地址 | none |
| »» liveLinkUrl | string   | true | none |      | none |
| »» id          | integer  | true | none |      | none |
| »» title       | string   | true | none | 名称   | none |
| » message      | string   | true | none |      | none |
| » status       | string   | true | none |      | none |

## POST 节目页面

POST /program/onAir

通过节目对应的programid和type，定位对应小节目，获取小节目信息和大节目的历史记录

### 请求参数

| 名称        | 位置    | 类型     | 必选  | 说明   |
| --------- | ----- | ------ | --- | ---- |
| programId | query | string | 否   | none |
| type      | query | string | 否   | none |
| session   | query | string | 否   | none |

> 返回示例

> 200 Response

```json
{"data":{"favoriteId":"","typeGroup":"","sign":"isAD","videoPicUrl":"","columnPicUrl1":"","source":"","title":"At Work Network","showDate":"2021-12-31","duration":"03:00:00","videoUrl":"","programState":"1","context":"","canDownload":1,"startTime":"10:00","stopTime":"13:00","id":2699889,"columnPicUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","day":"2021-12-31","adText":"","info":"At Work Network on HITFM","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/5CE8B971AE6F49C095C2CAB7872D70EC.mp3","hasDocument":0,"hosts":[],"author":"","length":"3H","countryRegionLimit":"","history":[{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/5CE8B971AE6F49C095C2CAB7872D70EC.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-31","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-31","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-31","programId":"2699889","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/B4525F35FBFA4A05BCF9E6BC8F398ED9.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-31","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-31","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-31","programId":"2699881","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/E49C8A37CACA4CD2A0CB3078F949D99F.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-30","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-30","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-30","programId":"2699840","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/11883ED7FA124556829457EBF55A217F.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-29","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-29","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-29","programId":"2699792","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/F9447EDFA23B43B9AED1903DC5231EBB.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-28","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-28","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-28","programId":"2699752","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1BCBDC5C2BBB448DA1F31930A68DD1A1.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-27","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-27","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-27","programId":"2699709","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/150C8A37644C464FAFD0F81CDBBA5131.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-24","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-24","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-24","programId":"2699614","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/8A4C5A5CEBC443B3B1F5A92CB591AE7F.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-23","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-23","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-23","programId":"2699561","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1190F522B2EF453AA8A4ED2F1B445693.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-22","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-22","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-22","programId":"2699520","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/914E6C0F249A4B1A9AA2B6C703F5EB45.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-21","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-21","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-21","programId":"321116","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/9A1A40F3798F456D887F707CCB129A52.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-20","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-20","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-20","programId":"321078","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/F7234A29F178488DAD6D85427B69FA65.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-17","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-17","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-17","programId":"320986","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/75B458E67A0B48F3B653E6E100106F0A.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-16","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-16","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-16","programId":"320945","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/32E52EC9D41A425298FED664DD4AF131.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-15","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-15","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-15","programId":"320904","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/F60827D928534CD0A90710E148AF318F.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-15","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-15","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-15","programId":"320895","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/463E873B80604C68BD99310468D79851.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-14","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-14","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-14","programId":"320865","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/96BD6D83229C4534BA9393AB1CDB86A9.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-10","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-10","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-10","programId":"320649","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1AB2B58D927A45738C1AE2EE602D8A54.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-09","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-09","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-09","programId":"320592","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/53709D0DA1804ED5B65168568B1D418A.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-08","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-08","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-08","programId":"320531","isFavorite":"0"},{"favoriteId":"","mediaUrl":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/CC6EDEAEE7BF404782FCC7958AD967C9.mp3","hasDocument":0,"length":"3H","countryRegionLimit":"","title":"At Work Network","showDate":"2021-12-07","backgroundPicUrl":"","programTitle":"At Work Network","groupName":"en","createTime":"2021-12-07","canDownload":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","detail":"At Work Network on HITFM","time":"10:00 - 13:00","picurl1":"","day":"2021-12-07","programId":"320466","isFavorite":"0"}],"sort":999,"videoPicUrl1":"","playLength":"3H","adInfoUrl":"","programTitle":"At Work Network","mediaUrl2":"","groupName":"en","selection":[],"createTime":"2021-12-31","programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","adImageUrl":"","picurl1":"","messageAuthorization":0,"categoryId":"0","programId":433,"isFavorite":0},"message":"接口请求成功。","status":"1"}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明   | 数据模型   |
| --- | ------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline |

### 返回数据结构

状态码 **200**

| 名称                      | 类型       | 必选   | 约束   | 中文名             | 说明   |
| ----------------------- | -------- | ---- | ---- | --------------- | ---- |
| » data                  | object   | true | none |                 | none |
| »» favoriteId           | string   | true | none |                 | none |
| »» typeGroup            | string   | true | none |                 | none |
| »» sign                 | string   | true | none |                 | none |
| »» videoPicUrl          | string   | true | none |                 | none |
| »» columnPicUrl1        | string   | true | none |                 | none |
| »» source               | string   | true | none |                 | none |
| »» title                | string   | true | none | 节目名字            | none |
| »» showDate             | string   | true | none | 节目日期            | none |
| »» duration             | string   | true | none | 时长              | none |
| »» videoUrl             | string   | true | none |                 | none |
| »» programState         | string   | true | none |                 | none |
| »» context              | string   | true | none |                 | none |
| »» canDownload          | integer  | true | none |                 | none |
| »» startTime            | string   | true | none | 开始时分            | none |
| »» stopTime             | string   | true | none | 结束时分            | none |
| »» id                   | integer  | true | none | 小节目id，和请求id保持一致 | none |
| »» columnPicUrl         | string   | true | none | 图片              | none |
| »» day                  | string   | true | none | 节目日期            | none |
| »» adText               | string   | true | none |                 | none |
| »» info                 | string   | true | none | 简介              | none |
| »» mediaUrl             | string   | true | none | 音频地址            | none |
| »» hasDocument          | integer  | true | none |                 | none |
| »» hosts                | [string] | true | none |                 | none |
| »» author               | string   | true | none |                 | none |
| »» length               | string   | true | none | 时长              | none |
| »» countryRegionLimit   | string   | true | none |                 | none |
| »» history              | [object] | true | none | 相关的历史节目列表       | none |
| »»» favoriteId          | string   | true | none |                 | none |
| »»» mediaUrl            | string   | true | none |                 | none |
| »»» hasDocument         | integer  | true | none |                 | none |
| »»» length              | string   | true | none |                 | none |
| »»» countryRegionLimit  | string   | true | none |                 | none |
| »»» title               | string   | true | none |                 | none |
| »»» showDate            | string   | true | none |                 | none |
| »»» backgroundPicUrl    | string   | true | none |                 | none |
| »»» programTitle        | string   | true | none |                 | none |
| »»» groupName           | string   | true | none |                 | none |
| »»» createTime          | string   | true | none |                 | none |
| »»» canDownload         | integer  | true | none |                 | none |
| »»» programUrl          | string   | true | none |                 | none |
| »»» detail              | string   | true | none |                 | none |
| »»» time                | string   | true | none |                 | none |
| »»» picurl1             | string   | true | none |                 | none |
| »»» day                 | string   | true | none |                 | none |
| »»» programId           | string   | true | none |                 | none |
| »»» isFavorite          | string   | true | none |                 | none |
| »» sort                 | integer  | true | none |                 | none |
| »» videoPicUrl1         | string   | true | none |                 | none |
| »» playLength           | string   | true | none |                 | none |
| »» adInfoUrl            | string   | true | none |                 | none |
| »» programTitle         | string   | true | none | 节目标题            | none |
| »» mediaUrl2            | string   | true | none |                 | none |
| »» groupName            | string   | true | none |                 | none |
| »» selection            | [string] | true | none |                 | none |
| »» createTime           | string   | true | none |                 | none |
| »» programUrl           | string   | true | none | 图片              | none |
| »» adImageUrl           | string   | true | none |                 | none |
| »» picurl1              | string   | true | none |                 | none |
| »» messageAuthorization | integer  | true | none |                 | none |
| »» categoryId           | string   | true | none |                 | none |
| »» programId            | integer  | true | none | 大节目id           | none |
| »» isFavorite           | integer  | true | none |                 | none |
| » message               | string   | true | none |                 | none |
| » status                | string   | true | none |                 | none |

## POST 历史节目接口

POST /program/historyList

通过大节目的programid 获得历史节目列表，能获得单个节目的信息：名称 日期 时间 programid(单个节目) 图片

### 请求参数

| 名称        | 位置    | 类型     | 必选  | 说明   |
| --------- | ----- | ------ | --- | ---- |
| category  | query | string | 否   | none |
| programId | query | string | 否   | none |
| page      | query | string | 否   | none |
| session   | query | string | 否   | none |
| sort      | query | string | 否   | none |

> 返回示例

> 200 Response

```json
{
    "favoriteId": "",
    "data": [
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1C036B4FB95D486EAE9B4B77A9C01B76.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-30",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-30",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-30",
            "programId": 2699849
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/07B550DB6C57456EA1BE9156183B80E4.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-29",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-29",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-29",
            "programId": 2699808
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/03B5EDD3A7BA4B3E9867B5E3E33FEC23.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-28",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-28",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-28",
            "programId": 2699761
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/DF6354D430E84FF8B4387E810216C8DD.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-27",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-27",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-27",
            "programId": 2699721
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/F0450BD72D9146A19719F6AD9127653C.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-24",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-24",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-24",
            "programId": 2699626
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/0F55B3014D5F4A84A90BC6A63A1793F4.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-23",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-23",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-23",
            "programId": 2699576
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/AE0FEABC2CC5414388D14D36CFD8ADB6.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-22",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-22",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-22",
            "programId": 2699530
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/C58B5489D45445CF91802738B1FC8D26.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-21",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-21",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-21",
            "programId": 2699491
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/888C750170D145679135055CA22103A1.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-20",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-20",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-20",
            "programId": 321086
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/0C6F044EF8C14077AE348ED0496DD518.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-17",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-17",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-17",
            "programId": 320997
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/61F3C65264A94C3BA3B1336A2B0C89E1.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-16",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-16",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-16",
            "programId": 320955
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/DD420686F7124814B27B47A7560E5D8F.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-15",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-15",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-15",
            "programId": 320910
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/55B37CF416734970B5FE14A1B3FE2453.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-13",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "01:58:46",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-14",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-13",
            "programId": 320854
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/49925B3EA44A449E9BBC892C48813F5D.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-10",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-10",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-10",
            "programId": 320661
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/BDABF84AF2C64D95B6C4FEE659EC5470.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-09",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-10",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-09",
            "programId": 320634
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/50D5783657A042AE8F5F482030D94630.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-08",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-08",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-08",
            "programId": 320545
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/BD37810B3DF243B18142D0E9AD38EF96.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-07",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-07",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-07",
            "programId": 320486
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/60DF4CBB8467406988F1AFEA9B4CE088.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-06",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-06",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-06",
            "programId": 320409
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/92F81E54962C4F0B8E98FFFCDBE23E0A.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-03",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-03",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-03",
            "programId": 320200
        },
        {
            "mediaUrl": "https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/FCE8A9651B08444485637B4364A2524C.mp3",
            "typeGroup": "",
            "length": "3H",
            "videoPicUrl": "",
            "countryRegionLimit": "",
            "sort": 999,
            "title": "Big Drive Home",
            "type": 0,
            "videoPicUrl1": "",
            "showDate": "2021-12-02",
            "backgroundPicUrl": "",
            "picurl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "duration": "03:00:00",
            "programTitle": "Big Drive Home",
            "groupName": "en",
            "videoUrl": "",
            "createTime": "2021-12-03",
            "canDownload": 0,
            "programUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
            "time": "16:00 - 19:00",
            "detail": "Big Drive Home on HITFM",
            "picurl1": "",
            "day": "2021-12-02",
            "programId": 320151
        }
    ],
    "totalPage": 18,
    "sign": "isAD",
    "pageSize": 20,
    "message": "获取节目回放信息列表成功。",
    "adInfoUrl": "",
    "logoUrl": "https://radio-res.cgtn.com/image/2009/1599793347441.jpg",
    "groupName": "en",
    "total": 359,
    "totalSize": 359,
    "adImageUrl": "",
    "picurl1": "",
    "adText": "",
    "info": "Big Drive Home on HITFM",
    "isFavorite": 0,
    "status": "1"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明   | 数据模型   |
| --- | ------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline |

### 返回数据结构

状态码 **200**

| 名称                    | 类型       | 必选   | 约束   | 中文名   | 说明   |
| --------------------- | -------- | ---- | ---- | ----- | ---- |
| » favoriteId          | string   | true | none |       | none |
| » data                | [object] | true | none |       | none |
| »» mediaUrl           | string   | true | none | 音频地址  | none |
| »» typeGroup          | string   | true | none |       | none |
| »» length             | string   | true | none | 时长    | none |
| »» videoPicUrl        | string   | true | none |       | none |
| »» countryRegionLimit | string   | true | none |       | none |
| »» sort               | integer  | true | none |       | none |
| »» title              | string   | true | none | 节目标题  | none |
| »» type               | integer  | true | none |       | none |
| »» videoPicUrl1       | string   | true | none |       | none |
| »» showDate           | string   | true | none | 节目日期  | none |
| »» backgroundPicUrl   | string   | true | none |       | none |
| »» picurl             | string   | true | none | 图片    | none |
| »» duration           | string   | true | none | 时长    | none |
| »» programTitle       | string   | true | none | 节目标题  | none |
| »» groupName          | string   | true | none |       | none |
| »» videoUrl           | string   | true | none |       | none |
| »» createTime         | string   | true | none | 节目日期  | none |
| »» canDownload        | integer  | true | none |       | none |
| »» programUrl         | string   | true | none | 图片    | none |
| »» time               | string   | true | none |       | none |
| »» detail             | string   | true | none | 节目详情  | none |
| »» picurl1            | string   | true | none |       | none |
| »» day                | string   | true | none | 节目日期  | none |
| »» programId          | integer  | true | none | 小节目id | none |
| » totalPage           | integer  | true | none | 总分页数  | none |
| » sign                | string   | true | none |       | none |
| » pageSize            | integer  | true | none | 分页大小  | none |
| » message             | string   | true | none |       | none |
| » adInfoUrl           | string   | true | none |       | none |
| » logoUrl             | string   | true | none | 图片    | none |
| » groupName           | string   | true | none |       | none |
| » total               | integer  | true | none | 总数量   | none |
| » totalSize           | integer  | true | none | 总数量   | none |
| » adImageUrl          | string   | true | none |       | none |
| » picurl1             | string   | true | none |       | none |
| » adText              | string   | true | none |       | none |
| » info                | string   | true | none | 节目详情  | none |
| » isFavorite          | integer  | true | none |       | none |
| » status              | string   | true | none |       | none |

## POST 搜索接口

POST /program/search

返回小节目的programid和type

### 请求参数

| 名称          | 位置    | 类型     | 必选  | 说明   |
| ----------- | ----- | ------ | --- | ---- |
| programName | query | string | 否   | none |

> 返回示例

> 200 Response

```json
{"data":[{"programTitle":"Lazy Afternoon","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748977739.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/4D92D294A75D4B53A2D1B9CE31EAA320.mp3","picurl1":"","title":"Lazy Afternoon","programId":2699888,"backgroundPicUrl":""},{"programTitle":"At Work Network","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/B4525F35FBFA4A05BCF9E6BC8F398ED9.mp3","picurl1":"","title":"At Work Network","programId":2699881,"backgroundPicUrl":""},{"programTitle":"At Work Network","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/5CE8B971AE6F49C095C2CAB7872D70EC.mp3","picurl1":"","title":"At Work Network","programId":2699889,"backgroundPicUrl":""},{"programTitle":"Hit Morning Show","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793717356.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/6391B145E72D43EB88D5B4BAFE18D5B8.mp3","picurl1":"","title":"Hit Morning Show","programId":2699876,"backgroundPicUrl":""},{"programTitle":"Morning Hits","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793944011.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/5358F24F5B0946778C25D82BEC7D67AB.mp3","picurl1":"","title":"Morning Hits","programId":2699869,"backgroundPicUrl":""},{"programTitle":"HitFM Dance","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748710201.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/9DEF87FF1FBB4425BA026BAB11CD1C2B.mp3","picurl1":"","title":"HitFM Dance","programId":2699864,"backgroundPicUrl":""},{"programTitle":"HitFM Dance","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748710201.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/4D0208AF808742E2B2DFC417FEDE85F6.mp3","picurl1":"","title":"HitFM Dance","programId":2699870,"backgroundPicUrl":""},{"programTitle":"New Music Express","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599794264630.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/DCCF2E6806E440B6AC13577A828BCBFA.mp3","picurl1":"","title":"New Music Express","programId":2699860,"backgroundPicUrl":""},{"programTitle":"Big Drive Home","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793347441.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1C036B4FB95D486EAE9B4B77A9C01B76.mp3","picurl1":"","title":"Big Drive Home","programId":2699849,"backgroundPicUrl":""},{"programTitle":"Lazy Afternoon","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748977739.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/C0F96CA04A304DAE9122CCBC829B8DFD.mp3","picurl1":"","title":"Lazy Afternoon","programId":2699843,"backgroundPicUrl":""},{"programTitle":"At Work Network","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/E49C8A37CACA4CD2A0CB3078F949D99F.mp3","picurl1":"","title":"At Work Network","programId":2699840,"backgroundPicUrl":""},{"programTitle":"Hit Morning Show","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793717356.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/DD701668C8494D30B0B1226A2EC83628.mp3","picurl1":"","title":"Hit Morning Show","programId":2699835,"backgroundPicUrl":""},{"programTitle":"Morning Hits","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793944011.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/266BF9CD711C4781A95FAD004C4632CA.mp3","picurl1":"","title":"Morning Hits","programId":2699832,"backgroundPicUrl":""},{"programTitle":"HitFM Dance","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748710201.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/6ED2F6DCDBCC4C69A0187FCAF4995366.mp3","picurl1":"","title":"HitFM Dance","programId":2699826,"backgroundPicUrl":""},{"programTitle":"New Music Express","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599794264630.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/6C32FC56C66E41C78D095035BB997E75.mp3","picurl1":"","title":"New Music Express","programId":2699819,"backgroundPicUrl":""},{"programTitle":"Big Drive Home","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793347441.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/07B550DB6C57456EA1BE9156183B80E4.mp3","picurl1":"","title":"Big Drive Home","programId":2699808,"backgroundPicUrl":""},{"programTitle":"Lazy Afternoon","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599748977739.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/4715124A30834764B9D88EF7248461D8.mp3","picurl1":"","title":"Lazy Afternoon","programId":2699800,"backgroundPicUrl":""},{"programTitle":"At Work Network","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599749513721.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/11883ED7FA124556829457EBF55A217F.mp3","picurl1":"","title":"At Work Network","programId":2699792,"backgroundPicUrl":""},{"programTitle":"Hit Morning Show","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793717356.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/628893FA28204F60A9709280845C8D82.mp3","picurl1":"","title":"Hit Morning Show","programId":2699787,"backgroundPicUrl":""},{"programTitle":"Morning Hits","programType":"5","canOpen":1,"programUrl":"https://radio-res.cgtn.com/image/2009/1599793944011.jpg","source":"https://radio-wdsl.cgtn.com/WJSL_YFMD/WJSL_YFMD/54c6f9582a80fc1e70ff5575/1F5F0F691026499F9DC0EC5AA81B7BC6.mp3","picurl1":"","title":"Morning Hits","programId":2699784,"backgroundPicUrl":""}],"message":"接口请求成功。","status":"1"}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明   | 数据模型   |
| --- | ------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | none | Inline |

### 返回数据结构

状态码 **200**

| 名称                  | 类型       | 必选   | 约束   | 中文名     | 说明   |
| ------------------- | -------- | ---- | ---- | ------- | ---- |
| » data              | [object] | true | none |         | none |
| »» programTitle     | string   | true | none | 节目标题    | none |
| »» programType      | string   | true | none | 小节目type | none |
| »» canOpen          | integer  | true | none |         | none |
| »» programUrl       | string   | true | none | 图片      | none |
| »» source           | string   | true | none | 音频链接    | none |
| »» picurl1          | string   | true | none |         | none |
| »» title            | string   | true | none | 节目标题    | none |
| »» programId        | integer  | true | none | 小节目id   | none |
| »» backgroundPicUrl | string   | true | none |         | none |
| » message           | string   | true | none |         | none |
| » status            | string   | true | none |         | none |

# 数据模型
