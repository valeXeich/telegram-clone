from typing import List

from db.models import Room, Message, User
from db.database import database


async def get_rooms(user: User):
    rooms = await user.rooms.select_related(['messages', 'messages__user']).all()
    rooms_with_last_message = []
    for room in rooms:
        user = await User.objects.select_related('rooms').filter(rooms__id=room.id).exclude(id=user.id).get()
        last_message = room.messages[-1] if room.messages else None
        room_dict = room.dict()
        if last_message:
            room_dict['message'] = last_message.dict()
        room_dict['user'] = user
        rooms_with_last_message.append(room_dict)
    return rooms_with_last_message


async def get_room(user: User, id: int):
    room = await Room.objects.prefetch_related(['messages', 'messages__user']).get_or_none(id=id)
    user = await User.objects.select_related('rooms').filter(rooms__id=room.id).exclude(id=user.id).get()
    room_dict = room.dict()
    room_dict['user'] = user
    return room_dict


async def create_message(message: dict, room_id: int, user: User):
    room = await Room.objects.get(id=room_id)
    message_copy = message.copy()
    message_copy.pop('created_at')
    message_copy.pop('user')
    message_copy.pop('encodedData', None)
    message = await Message.objects.create(
        **message_copy,
        user=user
    )
    await room.messages.add(message)
    return message


async def set_readed_to_messages(messages_id: List[int]):
    async with database.transaction():
        messages = await Message.objects.filter(id__in=messages_id).all()
        for message in messages:
            message.readed = True
        await Message.objects.bulk_update(messages, ['readed'])
