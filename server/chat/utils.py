import base64
from datetime import datetime, timedelta

import aio_pika
import aiofiles


def format_created_at(created_at):
    time_elapsed = datetime.now() - created_at

    if time_elapsed < timedelta(days=1):
        return created_at.strftime("%I:%M %p")

    elif time_elapsed < timedelta(days=2):
        return "Yesterday"

    elif time_elapsed < timedelta(days=7):
        return created_at.strftime("%A")

    else:
        return created_at.strftime("%m/%d/%Y")


async def save_media(message):
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = message['file_name']
    file_name = f'{time_string}_{file_name}'
    binary_data = base64.b64decode(message['encodedData'])
    print(len(binary_data))
    file_path = f'media/{file_name}'
    async with aiofiles.open(file_path, mode='wb') as f:
        await f.write(binary_data)
    return file_path


async def on_message(message: aio_pika.IncomingMessage):
    msg = message.body.decode("utf-8")
    return msg