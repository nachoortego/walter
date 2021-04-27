from binan import binan 

coin, pair = '', ''


async def findPrice(message):
    for i in binan.list:
        if message.content.upper() == i:
            await message.channel.send('{0:.2f}'.(binan.getPrice(i.upper())))


async def crypto(message):
    content = ''
    price = 0.0
    for i in binan.list:
        if 'BTCUSDT' in i or 'ETHUSDT' in i or 'ADAUSDT' in i or 'DOTUSDT' in i or 'BNBUSDT' in i or 'DOGEUSDT' in i:
            price = binan.getPrice(i)
            content = i.replace('USDT', '')
            price = '{0:.2f}'.format(float(price))
            content += f' = {price}'
            await message.channel.send(str(content))
    await message.channel.send('Fuente: https://binance.com')


