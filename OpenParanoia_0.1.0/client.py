import asyncio
import websockets
with open('config.json', 'r') as file:
    config = json.loads(file.read())
    ws_server_port=config["ws_server_port"]

async def send_message():
    url="ws://127.0.0.1"+str(ws_server_port)
    async with websockets.connect(url) as websocket:
        while True:
            ip = input("\033[1;46m>\033[0m")
            await websocket.send(ip)
            print("\033[42m 正在思考喵~ +\033[0m")
            callback = await websocket.recv()
            print(callback)
while True:
    print("OpenParanoia \033[1;36mClient\033[0m")
    asyncio.run(send_message())