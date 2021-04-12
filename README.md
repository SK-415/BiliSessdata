# BiliSessdata

## 这是什么？

共享一个 B站 的 SESSDATA，每天自动更新，保证长期有效。

这个项目主要是为了让 [HarukaBot](https://github.com/SK-415/HarukaBot) 用户不登录也可以请求一些需要 SESSDATA 的 API。如果你碰巧有类似需求，请随意取用。

## 那么什么是 SESSDATA？

SESSDATA 是 B站 的登陆凭证，每个账户登录后都会在服务器生成一个单独的 SESSDATA，如果不刷新有效期为半个月。可以用 SESSDATA 来请求某些必须要登录状态才能访问的 API，具体可以参考 [易姐的文档](https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/other/API_auth.md)。

注意，SESSDATA 本身只具备**查看**权限，任何操作类 API，如点赞、投币、评论都需要和 bili_jct 配合使用。

## 所以为什么不提供 bili_jct？

本项目只是提供一个方便**查看** B站 API 的身份，并无意对 B站 数据产生实质性操作。同时也杜绝被滥用的风险。

## 使用方法

数据储存在根目录的 `SESSDATA` 文件，直接访问其原始数据即可使用。每天会在北京时间 `00: 00` 自动刷新 Token，延长有效时间。届时 SESSDATA 的值也会更新，旧值会直接失效，请写好相应的异常处理，及时更新。

### 请求链接

三个链接任选其一，如果 GitHub 连不上可以考虑使用 FastGit 或者 JsDelivr。

- GitHub：https://raw.githubusercontent.com/SK-415/BiliSessdata/main/SESSDATA
- FastGit：https://raw.fastgit.org/SK-415/BiliSessdata/main/SESSDATA
- jsDelivr: https://cdn.jsdelivr.net/gh/SK-415/BiliSessdata@main/SESSDATA

### 返回格式

|字段|类型|内容|
|---|---|---|
|value|str|SESSDATA|
|updated|str|最后更新时间|

### 返回示例

```json
{"value": "41726716%2C1620771645%2C18206041", "updated": "2021-04-12 06:20:47 CST"}
```

## 支持与贡献

如果这个项目对你有帮助不妨点个 Star 吧，如果有什么改进建议也欢迎提交 Issue 和 Pull requests。

## 免责申明

本项目仅供学习交流使用，请勿用于任何违法、商业用途。