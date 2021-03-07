import discord
from config import settings
import json
import requests
import time
start_time = str()
bot = discord.Client()
@bot.event
async def on_message(message):
#Base information collect
    global start_time
    channel = message.channel
    try:
        f = open(f'rules/rules{channel.id}.txt', 'r')
        can_raw = f.read()
        print(can_raw)
        can = eval(can_raw)['var']
        #print(can)
        f.close()
    except FileNotFoundError:
        can = 'True'
    # print(message)
    msg_inf = str(str(channel) + ' ' + str(message.author) + ' ' + str(message.content) +  ' CanSend:' + str(can))
    try:
        msg_pict = message.attachments[0].url
        for_log = str(str(msg_inf) + ' ' + str(msg_pict))
    except IndexError:
        for_log = str(msg_inf)
    #print(for_log)
    f = open('log.txt', 'a')
    f.write(str(for_log + '\n'))
    f.close()
#Base information collect end
    if can == 'True':
        if message.content.startswith('!random'):
            try:
                msg = message.content.split(sep=' ')[1]
            except IndexError:
                await channel.send(
                '!random <thing>\n Оно может выслать:\nФакты: dogFact, catFact, pandaFact, foxFact, '
                'birdFact, '
                'koalaPict\nКартинки:dogPict, catPict, pandaPict, foxPict, birbPict, red_pandaPict, koalaPict, '
                'pikachu, meme')
            if msg == 'dogPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/dog')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random dog')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'catPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/cat')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random cat')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'pandaPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/panda')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random panda')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'foxPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/fox')
                    json_data = json.loads(response.text)
                    print(json_data['link'])
                    embed = discord.Embed(color=0xff9900, title=f'Random fox')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                    # link = json_data['link']
                    # await channel.send(f'Random fox\n{link}')
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'birbPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/birb')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random birb')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'koalaPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/koala')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random koala')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'red_pandaPict':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/red_panda')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random koala')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'pikachu':
                try:
                    response = requests.get(f'https://some-random-api.ml/img/pikachu')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=f'Random koala')
                    embed.set_image(url=json_data['link'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')
            if msg == 'meme':
                try:
                    response = requests.get(f'https://some-random-api.ml/meme')
                    json_data = json.loads(response.text)
                    embed = discord.Embed(color=0xff9900, title=json_data['caption'])
                    embed.set_image(url=json_data['image'])
                    await channel.send(embed=embed)
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужное изображение')

            if msg == 'dogFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/dog')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            if msg == 'catFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/cat')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            if msg == 'pandaFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/panda')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            if msg == 'foxFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/fox')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            if msg == 'birdFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/bird')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
            if msg == 'koalaFact':
                try:
                    response = requests.get(f'https://some-random-api.ml/facts/koala')
                    json_data = json.loads(response.text)
                    await channel.send(json_data['fact'])
                except json.decoder.JSONDecodeError:
                    await channel.send('Ошибка, невозможно найти нужный факт')
        if message.content.startswith('!bot'):
            if msg == 'help':
                await channel.send('''Команды:
            !random - прислать рандомную штуку
            !bot - обратиться к боту
            чтобы узнать подробнее надо набрать '<команда> help'
            пока что их всего две, но какие!
            This bot was made by ♂TheSaintDiratof♂
            Хы) чиста велосипедист''')
            if msg == 'upTime':
                uptime = int(time.strftime('%s')) - int(start_time)
                uptime_sec = uptime % 60
                uptime_min_raw = uptime // 60
                uptime_min = uptime_min_raw % 60
                uptime_h_raw = uptime // 3600
                uptime_h = uptime_h_raw % 24
                uptime_day = uptime_h_raw // 24
                seconds = '0'
                minuts = '0'
                hours = '0'
                days = '0'
                if str(uptime_sec)[-1] == '1':
                    seconds = ' секунда '
                if int(str(uptime_sec)[-1]) >= 2:
                    seconds = ' секунды '
                if int(str(uptime_sec)[-1]) >= 5 or int(str(uptime_sec)[-1]) == 0:
                    seconds = ' секунд '
                if int(str(uptime_min)[-1]) == 1:
                    minuts = ' минута, '
                if int(str(uptime_min)[-1]) >= 2:
                    minuts = ' минуты, '
                if int(str(uptime_min)[-1]) >= 5 or int(str(uptime_min)[-1]) == 0:
                    minuts = ' минут, '
                if int(str(uptime_h)[-1]) == 1:
                    hours = ' час, '
                if int(str(uptime_h)[-1]) >= 2:
                    hours = ' часа, '
                if int(str(uptime_h)[-1]) >= 5 or int(str(uptime_h)[-1]) == 0:
                    hours = ' часов, '
                if int(str(uptime_day)[-1]) == 1:
                    days = ' день, '
                if int(str(uptime_day)[-1]) >= 2:
                    days = ' дня, '
                if int(str(uptime_day)[-1]) >= 5 or int(str(uptime_h)[-1]) == 0:
                    days = ' дней, '
                # for_send = str(uptime_sec) + seconds + str(uptime_min) + minuts
                for_send = str(uptime_day) + days + str(uptime_h) + hours + str(uptime_min) + minuts + str(
                    uptime_sec) + seconds
                await channel.send(for_send)
        if message.content.startswith('!help'):
            try:
                msg = message.content.split(sep=' ')[1]
                if msg == 'help':
                    await channel.send('Ты дурачок? Или любитель писать \'man man\' в консоли?')
                if msg == 'bot':
                    await channel.send('''Имеет следующие аргументы:
    CanSend - имеет следующие аргументы:
        set - имеет следующие аргументы:
            True - разрешает боту писать в канал
            False - запрещает боту писать в канал
        check - проверяет запрет на отсылку сообщений в канал
    upTime - показывает, сколько времени прошло со старта бота''')
                if msg == 'random':
                    await channel.send('''!random <thing>
    Оно может выслать:
    Факты: dogFact, catFact, pandaFact, foxFact, birdFact, koalaPict
    Картинки:dogPict, catPict, pandaPict, foxPict, birbPict, red_pandaPict, koalaPict, pikachu, meme''')
            except:
                channel.send('''У данного бота есть следующие команды:
    !bot - возможность запретить(разрешить) отправлять сообщения в данный канал, посмотреть аптайм
    !rndm - скинуть рандомную штуку
    чтобы подробнее узнать о командах наберите '!help <команда без \'!\'>''')
        '''if message.content.startswith('!ban'):
            try:
                msg = message.content.split(sep=' ')[1]
                try:
                    reason = message.content.split(sep=' ')[2]
                except IndexError:
                    reason = 'Причина не указана'
                if reason == None:
                    await channel.send(f"Woah {message.author.mention}, Make sure you provide a reason!")
                else:
                    messageok = f"{msg} has been banned from {message.author.guild.name} for {reason}"
                    await channel.send(messageok)
                    await msg.ban(reason=reason)
            except IndexError:
                await channel.send('Кого банить?')'''
    else:
        await channel.send('Ты так никуда не дозвонишься.... Надо включить возможность писать в канал')

@bot.event
async def on_message(message):#здесь все самое необходимое, что должно работать даже при выключенной возможности писать в канал
    global start_time
    msg_inf = str(str(message.channel) + ' ' + str(message.author) + ' ' + str(message.content) +  ' !Base comand!')
    try:
        msg_pict = message.attachments[0].url
        for_log = str(str(msg_inf) + ' ' + str(msg_pict))
    except IndexError:
        for_log = str(msg_inf)
    #print(for_log)
    f = open('log.txt', 'a')
    f.write(str(for_log + '\n'))
    f.close()
    if message.content.startswith('!bot'):
        msg = message.content.split(sep=' ')[1]
        try:
            msg_2 = message.content.split(sep=' ')[2]
        except IndexError:
            msg_2 = 'help'
        if msg == 'CanSend':
            print(msg)
            if msg_2 == 'set':
                try:
                    msg_3 = message.content.split(sep=' ')[3]
                except IndexError:
                    await message.channel.send('Введите значение(True,False)')
                if msg_3 == 'True' or msg_3 == 'False':
                    print(msg_3)
                    for_file = str({'var': msg_3,
                                    'who': message.author.name,
                                    'when': time.strftime('%d.%m.%y; %H:%M:%S')}) + '\n'
                    # print(for_file)
                    f = open(f'rules/rules{message.channel.id}.txt', 'w')
                    f.write(for_file)
                    await message.channel.send('Правило создано')
                else:
                    await message.channel.send('Допустимые значения:False, True')
            if msg_2 == 'check':
                try:
                    f = open(f'rules/rules{message.channel.id}.txt', 'r')
                    rules = eval(f.read())
                    f.close()
                    # print(rules)
                    for_send = str('Значение:' + str(rules['var']) +
                                   '\nКто создал: ' + str(rules['who'] +
                                                          '\nКогда создал: ' + str(rules['when'])))
                    await message.channel.send(for_send)
                except FileNotFoundError:
                    await message.channel.send('Правило не создано')
            if msg_2 == 'help':
                await message.channel.send('check - посмотреть правила\n set - установить\n help - просмотреть данное сообщение')


@bot.event
async def on_ready():
    #On startup log
    global start_time
    start_time = time.strftime('%s')
    for_log = 'Logged in as\n'
    for_log = 'Time is: ' + time.strftime('%d.%m.%y; %H:%M:%S\n')
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