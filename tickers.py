from trader import broker

coin, pair = '', ''


async def findPrice(message):
    for i in broker.list:
        if message.content == i:
            await message.channel.send(broker.getPrice(i))


async def crypto(message):
    content = ''
    price = 0.0
    for i in broker.list:
        if 'BTCUSDT' in i or 'ETHUSDT' in i or 'ADAUSDT' in i or 'DOTUSDT' in i or 'BNBUSDT' in i:
            price = broker.getPrice(i)
            content = i.replace('USDT', '')
            price = '{0:.2f}'.format(float(price))
            content += f' = {price}'
            await message.channel.send(str(content))
    await message.channel.send('Fuente: https://binance.com')


