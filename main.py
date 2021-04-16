import discord
import tickers
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('discord_secret')
client = discord.Client()

prefix = '='


@client.event
async def on_ready():
    print('Estoy vivo como {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hola'):
        await message.channel.send('hola trolazo')
    
    await tickers.findPrice(message)

    if message.content.startswith(prefix):
        if 'crypto' in message.content:
            await tickers.crypto(message)

client.run(TOKEN)
