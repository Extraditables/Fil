import discord
import discord.ext
import random
import asyncio
import datetime
import json
import requests

from discord.ext import commands

hello_words = ["-фил привет", "-фил", "-фил ку", "-филипп", "-фил здарова", "-здарова", "-привет"]
info_words = ["-как дела?", "-как дела", "-как настроение?", "-как настроение", "-как ты?", "-как ты", "-как жизнь?",
              "-как "
              "жизнь"]

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()
    msg_list = msg.split()
    # if msg in hello_words or (len(list(set(msg_list + hello_words))))<len(msg_list) + len(hello_words):
    find_hello_words = False
    for item in hello_words:
        if msg.find(item) >= 0:
            find_hello_words = True
    if (find_hello_words):
        await message.channel.send('Привет')

    find_info_words = False
    for item in info_words:
        if msg.find(item) >= 0:
            find_info_words = True
    if (find_info_words):
        await message.channel.send('Хорошо')

    if message.content.startswith('Люблю Леру'):
        await message.channel.send('И я люблю :heart:')
    elif message.content.startswith('Люблю Лисёнка'):
        await message.channel.send(':heart: :fox:')
    elif message.content.startswith('Чей ты сын?'):
        await message.channel.send('Asyna#5837 и zxcmode#4104')
    if message.content.startswith('люблю леру'):
        await message.channel.send('И я люблю :heart:')
    if message.content.startswith('346346346346346346346'):
        await message.channel.send(
            '``` 1. Запрещены оскорбления, провокации в сторону участников сервера. Наказание по '
            'этому пункту выдаётся только при наличии жалоб и конфликтов.\n 2. Реклама строго '
            'запрещена.\n 3. Запрещено выпрашивать роли / доступ к комнатам(роли и доступ к '
            'комнатам даются по доверию).\n 4. Запрещается публикация материалов грубого, '
            'насильственного характера, жестокости.\n 5. Запрещается дискриминация по любому '
            'признаку — расовому, национальному, гражданскому, половому, религиозному, '
            'возрастному, по инвалидности, роду занятий или сексуальной ориентации(наказание '
            'будет принято в случае жалобы от лица которого оскорбляли).\n 6. Запрещается '
            'цитировать личную переписку из привата или других средств общения одних '
            'участников сервера с другими без явного согласия обеих сторон.\n 7. Запрещается '
            'разглашение чьей бы то ни было персональной информации (например, '
            'такой как адреса, телефоны, email, финансовых данных, перепост личных фото '
            'участников сервера, профилей в соцсетях и пр.). Это относится как к собственным '
            'данным, так и полученным от других пользователей.\n 8. Запрещена публикация '
            'сообщений, призывающих к суициду.\n 9. Незнание правил не освобождает от '
            'ответственности.\n 10. Запрещается публичное осуждение действий представителей '
            'TTS (To The Skies) - администраторов,  модераторов, хелперов. Если вы уверены, '
            'что кто-то превышает свои полномочия, обратитесь к администрации.\n 11. '
            'Администрация сервера в праве в любой момент, прекратить предоставление доступа к '
            'серверу конкретному пользователю.```')


print('start')

client.run('***')
