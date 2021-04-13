import discord
import tickers

TOKEN = 'NzIyNjEyMTAxOTQzNzg3NTgw.Xulm9g.rhEA4Kd9O4QZ_QM1wxRKrVOL0a0'
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
