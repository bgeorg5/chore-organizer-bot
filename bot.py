import discord
import responses
import credentials
from _collections_abc import Mapping
from _collections_abc import MutableMapping
from _collections_abc import Sequence

async def send_message(message, username, nickname, user_message, is_private):
    try:
        response = responses.handle_response(username, nickname, user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = credentials.token()
    client = discord.Client(intents=discord.Intents.default())

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return 

        print(f'client.user: {client.user}')
        print(f'message.author: {message.author}')
        print(f'message.author.name: {message.author.global_name}')
        print(f'message.author.nick: {message.author.nick}')
        print(f'message: {message}')
    
        username = str(message.author.name)
        nickname = str(message.author.nick)

        if nickname == 'None':
            nickname = str(message.author.global_name)
            print(f'NEW NICKNAME: {nickname}')

        user_message = str(message.clean_content)[11:] ##Removes the bots name attached to the message, str(message.content)[23:]
        channel = str(message.channel)

        print(f" --- \n {username} (nick:{nickname}) said '{user_message}' in {channel} \n --- ")

        ##if the user starts the message with a '?' then they want a private message
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message=message, username=username, nickname=nickname, user_message=user_message, is_private=True)
        else:
            await send_message(message=message, username=username, nickname=nickname, user_message=user_message, is_private=False)

        ##responses.handle_response(message=message)

    client.run(TOKEN)







