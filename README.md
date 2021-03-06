# O365-Client

![GitHub All Releases](https://img.shields.io/github/downloads/Fuider/O365-Client/total?label=release%20downloads&logo=Github&style=flat-square) 
![Telegram Group](https://img.shields.io/badge/dynamic/json?color=blue&label=Telegram%20Group&query=%24.data.totalSubs&url=https%3A%2F%2Fapi.spencerwoo.com%2Fsubstats%2F%3Fsource%3Dtelegram%26queryKey%3Dfuider)

这个分支将不会很快翻译成英文，因为正在开发。  **This branch won't be translated in a short time, because we are still developing.**

这个分支还有bug, 我们大约还会在修复半年左右。再往后，我们将不再维护这个分支，我们将在Fix分支上面重构它。

本程序真实维护人,主要人员:Micraow
![GitHub followers](https://img.shields.io/github/followers/micraow?color=red&label=My%20followers&logo=Github&logoColor=blue&style=flat-square)
, xiaocao162020, ella

在为本项目做出贡献前，请仔细阅读 python-o365 项目的文档，及全部代码 [传送门](https://github.com/O365/python-o365)

此项目(O365-Client)为原 OMM(O365-Mail-Manager)项目

用 Python 编写的代码示例，与 O365 连接并查阅邮件，查看日历等。我们的梦想是尽可能多的集成 API。

~~欢迎大家前往[Microsoft Graph 项目](https://github.com/Fuider/MSGraph-Client)！~~

# 联系

如果您遇到问题，或是有任何建议，欢迎联系我们：邮件：[pengbo@pengbo0708.onmicrosoft.com](mailto:pengbo@pengbo0708.onmicrosoft.com), Telegram 用户群：[点击这里](https://t.me/fuider)。

# 注意

Bug 已解决，但相关方法尚未集成。

# 公告

1. 我们改变了开发方向，决定不再只针对于 O365 用户服务，而是所有微软用户，这意味着后续 Planner,Azure Direction 等 API 不会加入。原因一是因为我们的时间不够，而是因为我们现在一位使用者都没有。

2. 由于此分支更改了 API,所需的权限,也就是日历的权限。所以需要重新验证授权。如果报错，可以先尝试删除目录底下的 o365_token.txt.

3. 我们是一群热爱计算机的学生，非微软官方。😂

**欢迎 Pull requests 和 Issues!**

这是我第一个独立的项目，希望大家支持。
~~自 2020.7.23 起，此项目将不再定期维护，但如果以后有时间，我将会继续做下去。~~
感谢 csdn 和电报中众多朋友的帮助，现在我决定继续维护这个项目。
程序很简单，通过我的应用 ID 和机密连接到你的账号，并操作，运用了一个模板 [O365](https://github.com/O365/python-o365 "O365").
如果你要使用，请：

# 用法

1. pip install O365
2. 准备一个微软账号 [注册](https://account.microsoft.com/account?lang=zh-cn) ，事实上我更推荐含 Office 365(现更名为 Microsoft 365)的 E5 开发者订阅（我用的就是这个比较靠谱，而且可以支持所有的 API），注册方法请自行百度。
3. 运行Client.py

## 关于 office 365 账户

有一位朋友跟我讲说他需要获取 office E5 订阅
那么我就在这里讲一下大致的步骤。

1. 访问微软的开发者网站 https://developer.microsoft.com/zh-cn/office

2. 按下"立即加入"，或"了解更多信息"，接下来你需要登录你注册的免费的微软账号。
   ![图片](https://share.pengbo.workers.dev/1595596248544.jpg)

3. 我们是一群热爱python的学生，非Microsoft官方。😂

4.然后你添加完之后就能拿到一个有 25 位用户许可证的 E5 订阅，包含了全套的 office 套件，可用来正版激活软件，就不用熊那些么盗版的激活工具了，只要登录你的账号就可以激活办公软件了，不止支持软件的激活，这个订阅还包括了每个用户都有 5 TB 的云存储空间，还有你可以给他们分配邮箱。我的做法是给我的朋友们分配了这些邮箱，然后我便可以与他们联系。
[Office 网页版](https://office.com)
[管理员网站](https://admin.microsoft.com)
如果想要正常使用所有功能，需要在管理员网站中为你的主账户，就是默认生成的那个账户，也就是管理员账户分配一个许可证(E5)
此时你所有的邮箱后缀都为.onmicrosoft.com 如果你想要自定义后缀的话，可以绑定自定义域名，当然这些都是后话了，请自行百度。

需要注意的是，这个订阅是会过期的！如果 90 天内不进行开发活动(其实也有自动续订的方法)，微软就会删除你的订阅，这里推荐一个自动续订的方法
https://blog.curlc.com/archives/687.html
如果你觉得我讲的不够详细。那么你可以看一看这篇文章。
https://blog.curlc.com/archives/599.html
提醒:onedrive 默认的存储容量为 1 TB，需要将他们手动改为 5 TB，当然，1TB=1024 GB，相当于百度网盘的容量。你如果直连下载 onedrive 的文件的话，速度可能只比百度云快一点点，虽然微软没有对其进行限速，因为 onedrive 的服务器在国外，你可以搭建 oneindex(如果你使用的是自己的应用 ID 和机密，还可以提高续订的概率，因为据说微软时看 API 的调用量判断你的开发是否活跃。使用本程序也可以调用 API，虽然调用的是我的[偷笑]但是你可以换成你的，具体怎么换？我过一段时间回写下来。) 或其他的索引，或者一些在线的工具获取下载直链，然后通过 idm 多线程下载速度很快。
具体如何更改 onedrive 的容量，请看这篇文章。
https://blog.curlc.com/archives/66.html


## 优点

1. 简洁，体积小
2. 后台自动刷新 token，无需烦恼
3. 基本符合类编程风格，开发人员看的时候省心
4. 使用公共客户端流，更安全！

## 使用场景

1. 大陆 O365 用户
   由于 GFW 的封锁，访问 O365 网页版服务时，加载 js，脚本，页面等会用很长时间，使用本程序就简化了这些，提高效率。
2. 轻度用户
   不经常看邮箱，日历，只偶尔看一下，不想要下载微软那么大的软件。
3. 即用即退的用户
   本程序登录简单，注销也简单。将...token.txt 删去即可。
4. 极客，发烧友
   在终端命令行操作，范儿立马就有了！
5. Python 爱好者，学者，小白
   并不是很难，可以做代码示例学习。

## TO-DO

- [x] 日历功能（读取）
- [x] 发送邮件
- [x] 公共客户端问题。
- [ ] 加载邮件全文(HTML)
- [ ] 加载用户邮件文件夹
- [ ] 允许用户在 txt 文件中编辑邮件，然后程序识别，发送，有利于排版。
- [ ] 删除邮件
- [ ] 标为已读
- [ ] 标为红旗
- [ ] 标为未读
- [x] 获取 object-id (后来发现不用获取)
- [ ] 新建日历日程
- [x] ”支持“ 功能
- [ ] 移动邮件
- [ ] 将日历功能集成到 Client.py
- [ ] 允许用户通过日程名称检索起始时间
- [ ] 解决 HTML 邮件图片异常的问题
- [ ] 加入 settings.py，允许用户切换显示语言（中、英），以 HTML 格式处理邮件还是纯文本。
- [ ] 移交项目。
- [ ] 通过邮件是否已读检索邮件。

## 更新日志

### 2020.7.24

我的开源项目 O365 Mail Manager 终于完工了，大家有兴趣的快去看看吧。
本次更新内容:

1. 使用公共客户端流 auth_flow_type=='public'
   (终于解决了困扰了我一天的难题)
2. 允许选择进入哪个邮箱文件夹
   当前有四个是支持的。
3. 将 start 方法从 email_actions 类中重构出来，使之成为 Start 类(应用入口)
4. 优化部分代码，使其符合类编程风格。(还没优化完全部)

喜欢的可以给个 star 或与我合作，谢谢你们给了我动力！

### 7.26

更新内容:
拉取至 Dreams-builder/O365-Client

### 7.27

有了最基础的发件功能。
xiaocao162020 加入！
支持多收件人，感谢 @xiaocao162020

### 8.8

发件功能基本实现，但 HTML 邮件处理要改善。

### 8.11

加入了最基础的日历功能。可以打印出来事件的名称和起终时间。

**注意！**
由于此分支更改了 API,所需的权限,也就是日历的权限。所以需要重新验证授权。如果报错，可以先尝试删除目录底下的 o365_token.txt
