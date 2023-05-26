from typing import List

import aio_pika
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect

from auth.oauth2 import get_current_user, get_current_user_ws
from chat import services, schemas
from .manager import manager


router = APIRouter(
    tags=['chat'],
    prefix='/chat'
)

@router.get('/rooms', response_model=List[schemas.RoomList])
async def get_rooms(user=Depends(get_current_user)):
    rooms = await services.get_rooms(user)
    return rooms


@router.get('/room/{id}', response_model=schemas.Room)
async def get_room(id: int, user=Depends(get_current_user)):
    room = await services.get_room(user, id)
    return room


@router.websocket('/ws/{room_id}')
async def chat(websocket: WebSocket, room_id: int, user=Depends(get_current_user_ws)):
    await manager.connect(websocket, room_id)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.handle_message(data['action'], data['data'], room_id, user)
    except WebSocketDisconnect:
        await manager.disconnect(websocket, room_id)


async def on_message(message: aio_pika.IncomingMessage):
    msg = message.body.decode("utf-8")
    return msg


@router.websocket('/ws/notification/{user_id}')
async def notification(websocket: WebSocket, user_id: int, user=Depends(get_current_user_ws)):
    await websocket.accept()
    connection = await aio_pika.connect("amqp://rmuser:rmpassword@rabbitmq/")
    channel = await connection.channel()
    queue = await channel.declare_queue(f'notification-{user_id}')
    await queue.consume(on_message, no_ack=True)
    try:
        while True:
            msg = await queue.consume(on_message, no_ack=True)
            await websocket.send_json(msg)
    except WebSocketDisconnect:
        pass
