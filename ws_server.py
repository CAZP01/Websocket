# main.py
import asyncio
import websockets
import json

async def handler(websocket):
    print("[SERVER] Client connected")
    try:
        async for message in websocket:
            print(f"[RECV] {message}")
            data = json.loads(message)
            # Kirim balasan
            response = {"status": "ok", "echo": data}
            await websocket.send(json.dumps(response))
    except websockets.exceptions.ConnectionClosedOK:
        print("[SERVER] Client disconnected")
    except Exception as e:
        print("[ERROR]", e)

async def main():
    port = 8080
    print(f"[SERVER] Running on ws://0.0.0.0:{port}")
    async with websockets.serve(handler, "0.0.0.0", port):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
