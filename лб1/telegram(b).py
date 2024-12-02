from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest

api_id = 'my id'
api_hash = 'my hash id'
phone = 'number phone'

client = TelegramClient('session_name', api_id, api_hash)

async def send_message(entity, message_text):
    await client.send_message(entity, message_text)
    print(f"Повідомлення надіслано до {entity}!")

with client:

    recipient = 'https://t.me/lizamrt169'  
    message = "Привіт) Це канал Тест!." 
    
    client.loop.run_until_complete(send_message(recipient, message))
