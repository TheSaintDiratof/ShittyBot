import discord
from discord.ext import commands
from config import settings
import json
import requests
#class discord.Client(*, loop=None, **options)
bot = commands.Bot(command_prefix='!')
print(discord.version_info)
print(settings)
@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.

@bot.event
async def on_message(message):
    channel = message.channel
    s = str(str(channel) + ' ' + str(message.author) + ' ' + str(message.content) + '\n')
    print(s)
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
rndmPctr - прислать случайную картинку
bot - обратиться к боту
чтобы узнать подробнее надо набрать '<команда> help'
пока что их всего две
This bot was made by ♂TheSaintDiratof♂''')
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена