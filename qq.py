import asyncio
import websockets
import json
import requests

with open('config.json', 'r') as file:
    config = json.loads(file.read())
    ws_server_port=config["ws_server_port"]
    napcat_wsc_port=config["napcat_wsc_port"]
    napcat_html_port=config["napcat_html_port"]
url="ws://127.0.0.1"+str(ws_server_port)




callback = ""
payload = {}
datastr = ""
async def main():
  print("\033[1;40mdebug:开始监听Napcat \033[0m")
  async with websockets.serve(receive_napcat, "localhost", napcat_wsc_port):
    await asyncio.Future() # 保持运行
async def receive_napcat(websocket):
  while True:
    receive_message = await websocket.recv()
    print("\033[1;40mdebug:接收到napcat消息："+receive_message+" \033[0m")
    receive_json = json.loads(receive_message)
    if receive_json["post_type"] == "message" and receive_json["message_type"] == "private":
        print("\033[1;40mdebug:消息类型为message，内容为："+receive_json["raw_message"]+"\033[0m")
        url="ws://127.0.0.1:"+str(ws_server_port)
        async with websockets.connect(url) as websocket:
            await websocket.send(receive_json["raw_message"])
            print("\033[42m 正在思考喵~ \033[0m")
            global callback
            callback = await websocket.recv()
            print(callback)
        global payload
        payload = {"user_id": receive_json["user_id"],"message": callback}
        url = "http://127.0.0.1:"+str(napcat_html_port)+"/send_private_msg"
        resp = requests.post(url, json=payload)
        print(resp.json())
while True:
    print("OpenParanoia \033[1;36mNapcat Client\033[0m")
    while True:
        asyncio.run(main())