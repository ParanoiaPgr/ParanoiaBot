<img title="" src="paranoiabot.jpg" alt="a7111006ef0a0ac4b508d94281cb9594.jpg" width="1882"> 

____

# 项目简介

  一个由Python编写的QQ聊天Bot小项目，由ParanoiaPgr开发

# 部署&启动教学

**1.准备**：

一个硅基流动api，NapcatQQ([NapNeko/NapCatQQ: Modern protocol-side framework based on NTQQ](https://github.com/NapNeko/NapCatQQ))，Python3

**2.下载**：

打开Powershell，输入以下命令

`git clone https://github.com/ParanoiaPgr/ParanoiaBot.git`

`cd ./ParanoiaBot`

`pip install -r requirements.txt`

**3.Napcat准备**

在 Napcat WebUI>网络配置 里添加Websocket客户端，url处填写`ws://localhost:8767`（可以在config.json里"napcat_wsc_port"字段修改端口号），消息格式选择String，并启用

添加HTTP服务器，Port处填写`8768`（可以在config.json里"napcat_http_port"字段修改端口号），并启用

4.硅基流动准备

准备好硅基流动的Api Key，在config.json里"api_key"字段后的引号里填入Api Key

**5.启动**

首先，启动NapcatQQ并登录

然后在项目文件夹里打开Powershell，输入以下命令

`python server.py`

`python qq.py`

如果要本地聊天，输入以下命令

`python client.py`






