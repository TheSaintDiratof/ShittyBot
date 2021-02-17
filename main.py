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

@bot.command()
async def rndPct(ctx):
    ss = 'cat'
    response = requests.get(f'https://some-random-api.ml/img/{ss}') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = f'Random {ss}') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed
@bot.event
async def on_message(message):
    channel = message.channel
    print(channel)
    msg = message.content.split(sep=' ')[1]
    print(message.content)
    print(msg)
    if message.content.startswith('rndmPctr'):
        #await channel.send(f'Send me that 👍 reaction, mate {msg}')
        #msg = message.content.split(sep=' ')[1]
        print(msg)
        #channel.send(str(msg))
        if msg != 'help':
            response = requests.get(f'https://some-random-api.ml/img/{msg}')  # Get-запрос
            json_data = json.loads(response.text)  # Извлекаем JSON
            embed = discord.Embed(color=0xff9900, title=f'Random {msg}')  # Создание Embed'a
            embed.set_image(url=json_data['link'])  # Устанавливаем картинку Embed'a
            await channel.send(embed=embed)  # Отправляем Embed
        else:
            await channel.send('https://some-random-api.ml/')
    if message.content.startswith('bot'):
        #msg = message.content.split(sep=' ')[1]
        print(msg)
        if msg != 'help':
            pass
        else:
            pass
            channel.send('''Команды:
            rndmPctr - прислать случайную картинку
            bot - обратиться к боту
            чтобы узнать подробнее надо набрать '<команда> help'
            пока что их всего две''')
bot.run(settings['token']) # Обращаемся к словарю settings с ключом token, для получения токена