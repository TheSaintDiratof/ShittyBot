import discord
from config import settings
import json
import requests
import time
bot = discord.Client()
@bot.event
async def on_message(message):
    channel = message.channel
    try:
        f = open(f'rules/rules{channel.id}.txt', 'r')
        can = eval(f.read())['var']
        f.close()
    except:
        can = 'True'
    # print(message)
    msg_inf = str(str(channel) + ' ' + str(message.author) + ' ' + str(message.content))
    try:
        msg_pict = message.attachments[0].url
        for_log = str(str(msg_inf) + ' ' + str(msg_pict))
    except IndexError:
        for_log = str(msg_inf)
    print(for_log)
    f = open('log.txt', 'a')
    f.write(str(for_log + '\n'))
    f.close()
    #print(can)
    if message.content.startswith('rndmPctr'):
        if can == 'True':
            msg = message.content.split(sep=' ')[1]
            print(msg)
            if msg != 'help':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/{msg}')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random {msg}')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            else:
                await channel.send('https://some-random-api.ml/')
        else:
            await channel.send('Ты так никуда не дозвонишься.... Надо включить возможность писать в канал')
    if message.content.startswith('rndmFact'):
        if can == 'True':
            msg = message.content.split(sep=' ')[1]
            print(msg)
            if msg != 'help':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/{msg}')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            else:
                await channel.send('https://some-random-api.ml/')
        else:
            await channel.send('Ты так никуда не дозвонишься.... Надо включить возможность писать в канал')
    if message.content.startswith('bot'):
        #if can == 'True':
        msg = message.content.split(sep=' ')[1]
        try:
            msg_2 = message.content.split(sep=' ')[2]
        except IndexError:
            msg = 'help'
        if msg == 'CanSend':
            if msg_2 == 'set':
                try:
                    msg_3 = message.content.split(sep=' ')[3]
                except IndexError:
                    await channel.send('Введите значение(True,False)')
                if msg_3 == 'True' or msg_3 == 'False':
                    for_file = str({'var': msg_3,
                                    'who': message.author.name,
                                    'when': time.strftime('%d.%m.%y; %H:%M:%S')})
                    print(for_file)
                    f = open(f'rules/rules{channel.id}.txt', 'w')
                    f.write(for_file)
                    await channel.send('Правило создано')
                else:
                    await channel.send('')
            if msg_2 == 'check':
                try:
                    f = open(f'rules/rules{channel.id}.txt', 'r')
                    rules = eval(f.read())
                    f.close()
                    print(rules['var'])
                    for_send = str('Значение:' + str(rules['var']) +
                                   '\nКто создал: ' + str(rules['who'] +
                                                          '\nКогда создал: ' + str(rules['when'])))
                    await channel.send(for_send)
                except FileNotFoundError:
                    await channel.send('Правило не создано')
            if msg_2 == 'help':
                await channel.send(
                    'check - посмотреть правила\n set - установить\n help - просмотреть данное сообщение')
        if can == 'True':
            if msg == 'help':
                await channel.send('''Команды:
                        rndmFact - прислать случайный факт
                        rndmPctr - прислать случайную картинку
                        bot - обратиться к боту
                        чтобы узнать подробнее надо набрать '<команда> help'
                        пока что их всего две
                        This bot was made by ♂TheSaintDiratof♂
                        Хы) скоро в дурку поеду''')
        else:
            await channel.send('Ты так никуда не дозвонишься.... Надо включить возможность писать в канал')
@bot.event
async def on_ready():
    for_log = 'Logged in as\n'
    for_log = for_log + str(bot.user.name) + '\n'
    for_log = for_log + str(bot.user.id) + '\n'
    for_log = for_log + str(discord.version_info) + '\n'
    for_log = for_log + str(settings) + '\n'
    for_log = for_log + '------' + '\n'
    print(for_log)
    f = open('log.txt', 'a')
    f.write(for_log)
    f.close()
bot.run(settings['token'])
