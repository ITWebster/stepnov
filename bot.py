import os
import discord
import responses
from decouple import config


# This function will send a message to the discord chat
async def send_messages(message, user_message, username, is_private):
    try:
        response = responses.die_rolls(user_message, username)
        if response:
            await message.author.send(response) if is_private else await message.channel.send(response)

        else:
            print("Response is empty, not sending.")

    except Exception as e:
        print(e)
        


#This function runs a discord bot
def run_discord_bot():
    TOKEN = config('DISCORD_TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):

        print(message.channel)
         
        if message.author == client.user:
            return

        print("Not client.user")

        username = message.author
        username = str(username.display_name)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message and user_message[0] == '?':
            user_message = user_message[1:]
            await send_messages(message, user_message, username, is_private=True)

        else:
            await send_messages(message, user_message, username, is_private=False)