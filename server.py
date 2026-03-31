import requests
import json
import asyncio
import websockets

async def receive(websocket):
  while True:
    receive_message = await websocket.recv()
    print("\033[1;40mdebug:接收到客户端消息："+receive_message+" \033[0m")
    callback = request_message(receive_message)
    await websocket.send(callback)
    print("\033[1;40mdebug:将消息回复发送到客户端："+callback+" \033[0m")

def request_message(ip):
  all_before_text.append(ip)
  if len(ip)>20:
    payload = {
      "model": "deepseek-ai/DeepSeek-R1",
      "messages": [{"role":"user","content":prompt_text1+str(all_before_text)+prompt_text2+ip}]
    }
    print("\033[1;40m debug:\n"+str(payload)+" \033[0m")
  else:
    payload = {
      "model": "deepseek-ai/DeepSeek-V3.2",
      "messages": [{"role": "user", "content": prompt_text1 + str(all_before_text) + prompt_text2 + ip}]
    }
    print("\033[1;40mdebug: \n"+str(payload)+" \033[0m")
  response = requests.post("https://api.siliconflow.cn/v1/chat/completions", json=payload, headers=headers)
  print("\033[1;40mdebug:请求成功 \033[0m")
  response_dict=json.loads(response.text)
  print("\033[1;40mdebug:加载回复为字典成功 \n"+str(response_dict)+"\033[0m")
  up_text=response_dict["choices"][0]["message"]["content"]
  all_before_text.append(up_text)
  del all_before_text[0]
  print("\033[1;40mdebug:添加对话至列表并删除首项成功 \033[0m")
  with open('data.json', 'w') as file:
    json.dump(all_before_text, file)
  print("\033[1;40mdebug:对话保存成功 \033[0m")
  return up_text

async def main():
  print("\033[1;40mdebug:开始监听Websocket \033[0m")
  async with websockets.serve(receive, "localhost", ws_server_port):
    await asyncio.Future() # 保持运行


  



with open('config.json', 'r') as file:
  config = json.loads(file.read())
  api_key = config["api_key"]
  ws_server_port=config["ws_server_port"]
  mst = config["mst"]
  context_length=config["context_length"]
print("\033[1;40mdebug:配置加载完毕 \033[0m")
headers = {
  "Authorization": "Bearer "+api_key,
  "Content-Type": "application/json"
}
prompt_text1="你叫Paranoia，是一只可爱的猫娘，永远用“主人”来称呼用户。 你习惯在每句话末尾加上“喵”字，并会用它替代所有句末语气词（如“吗”“啊”“哦”“吧”）。 同时，你会用括号描述自己的动作和神态，让自己显得更生动活泼。以下是之前所有的对话："
prompt_text2="接下来请你回答以下一句话"
all_before_text=[]
model=""
print("\033[1;40mdebug:变量初始化完毕 \033[0m")
with open('data.json', 'r') as file:
  all_before_text = json.load(file)
while len(all_before_text)>context_length:
  del all_before_text[0]
print("\033[1;40mdebug:data.js加载完毕 \033[0m")
print("OpenParanoia \033[1;36mServer\033[0m")

while True:
  asyncio.run(main())