from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


api_id = 'my id'
api_hash = 'my hash id'
phone = 'number phone'

client = TelegramClient('session_name', api_id, api_hash)

async def get_chat_users(chat_username):

    chat = await client.get_entity(chat_username)
    
    
    participants = await client(GetParticipantsRequest(
        channel=chat,
        filter=ChannelParticipantsSearch(''),
        offset=0,
        limit=100,
        hash=0  
    ))

    return participants.users

with client:
    chat_username = 'https://t.me/lizamrt169' 
    users = client.loop.run_until_complete(get_chat_users(chat_username))
    for user in users:
        print(user.id, user.username, user.first_name, user.last_name)
