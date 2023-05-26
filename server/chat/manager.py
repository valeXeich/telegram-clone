import json
from typing import Dict, List

import aio_pika
from fastapi import WebSocket

from chat import services, schemas
from .utils import save_media


class ConnectionManager:
    def __init__(self):
        self.active_connections: Dict[int, List[WebSocket]] = {}

    async def connect(self, websocket: WebSocket, room_id: int):
        await websocket.accept()
        room = self.active_connections.get(room_id)
        if room:
            room.append(websocket)
        else:
            self.active_connections[room_id] = [websocket]
        await self.send_total_connections(room_id)

    async def send_total_connections(self, room_id):
        total_connections = self.get_total_connections(room_id)
        await self.broadcast({'online': total_connections}, room_id)

    async def disconnect(self, websocket: WebSocket, room_id: int):
        room = self.active_connections.get(room_id)
        if room:
            room.remove(websocket)
        await self.send_total_connections(room_id)

    def get_total_connections(self, room_id):
        room = self.active_connections.get(room_id)
        return len(room) if room else 0

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_json(message)

    async def broadcast(self, message: str, room_id: int):
        room = self.active_connections.get(room_id)
        if room:
            for connection in room:
                await connection.send_json(message)
    
    async def send_rabbitmq(self, message: dict, room_id: int):
        room = self.active_connections.get(room_id)
        rabbit_connection = await aio_pika.connect("amqp://rmuser:rmpassword@rabbitmq/")
        channel = await rabbit_connection.channel()

        for connection in room:
            await channel.default_exchange.publish(
                aio_pika.Message(json.dumps(message).encode("utf-8")),
                routing_key = f"notification-{connection.user.id}"
            )

        await rabbit_connection.close()

    async def handle_message(self, action: str, data, room_id: int, user: schemas.User):
        if action == 'update':
            await services.set_readed_to_messages(data)
        elif action == 'send':
            if data.get('is_file'):
                file_path = 'http://127.0.0.1:8000/' + await save_media(data)
                data['file'] = file_path
            message = await services.create_message(data, room_id, user)
            data['id'] = message.id
            await self.broadcast(data, room_id)
            await self.send_rabbitmq(message, room_id)

manager = ConnectionManager()
