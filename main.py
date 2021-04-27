import discord
import pipe
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
TOKEN = os.getenv('discord_secret')
client = discord.Client()

prefix = '='

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


@client.event
async def on_ready():
    print('Estoy vivo como {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hola'):
        await message.channel.send('hola trolazo')

    await pipe.findPrice(message)

    if message.content.startswith(prefix):
        if 'crypto' in message.content:
            await pipe.crypto(message)
            await message.channel.send(current_time)

async def help():
    embed = discord.Embed(tittle='Walter-Binance Help', description='A list of the discord commands for the Binance API')




client.run(TOKEN)
