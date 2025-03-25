import socketio
from fastapi import FastAPI
import uvicorn

app = FastAPI()
sio = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
socket_app = socketio.ASGIApp(sio, app)

@app.get("/")
async def root():
    return {"status": "LIMINA AI Server online!"}

@sio.event
async def connect(sid, environ):
    print(f"LIMINA connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"LIMINA disconnected: {sid}")

@sio.event
async def brainwave_data(sid, data):
    print(f"Incoming LIMINA data: {data}")

if __name__ == '__main__':
    uvicorn.run(socket_app, host='0.0.0.0', port=8000)
