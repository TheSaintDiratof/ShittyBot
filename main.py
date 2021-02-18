import discord
#from discord.ext import commands
from config import settings
import json
import requests
#class discord.Client(*, loop=None, **options)
bot = discord.Client()#client = discord.Client()
#bot = commands.Bot(command_prefix='!')
print(discord.version_info)
print(settings)
@bot.event
async def on_message(message):
    channel = message.channel
    s = str(str(channel) + ' ' + str(message.author) + ' ' + str(message.content) + '\n')
    print(s)
    print(message.embeds)
    f = open('log.txt', 'a')
    f.write(s)
    f.close()
    #try:
        #msg = message.content.split(sep=' ')[1]
    #except IndexError:
        #pass
    #print(msg)
    if message.content.startswith('rndmPctr'):
        #await channel.send(f'Send me that 👍 reaction, mate {msg}')
        msg = message.content.split(sep=' ')[1]
        print(msg)
        #channel.send(str(msg))
        if msg != 'help':
            try:
                response = requests.get(f'https://some-random-api.ml/img/{msg}')  # Get-запрос
                json_data = json.loads(response.text)  # Извлекаем JSON
                embed = discord.Embed(color=0xff9900, title=f'Random {msg}')  # Создание Embed'a
                embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
                await channel.send(embed=embed)  # Отправляем Embed
            except json.decoder.JSONDecodeError:
                await channel.send('Ошибка, невозможно найти нужное изображение')
        else:
            await channel.send('https://some-random-api.ml/')
    if message.content.startswith('rndmFact'):
        #await channel.send(f'Send me that 👍 reaction, mate {msg}')
        msg = message.content.split(sep=' ')[1]
        print(msg)
        #channel.send(str(msg))
        if msg != 'help':
            try:
                response = requests.get(f'https://some-random-api.ml/facts/{msg}')  # Get-запрос
                json_data = json.loads(response.text)  # Извлекаем JSON
                #embed = discord.Embed(color=0xff9900, title=f'Random {msg}')  # Создание Embed'a
                await channel.send(json_data['fact'])  # Отправляем Embed
            except json.decoder.JSONDecodeError:
                await channel.send('Ошибка, невозможно найти нужный факт')
        else:
            await channel.send('https://some-random-api.ml/')
    if message.content.startswith('bot'):
        msg = message.content.split(sep=' ')[1]
        print(msg)
        if msg != 'help':
            pass
        else:
            pass
            await channel.send('''Команды:
rndmFact - прислать случайный факт
rndmPctr - прислать случайную картинку
bot - обратиться к боту
чтобы узнать подробнее надо набрать '<команда> help'
пока что их всего две
This bot was made by ♂TheSaintDiratof♂''')
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена