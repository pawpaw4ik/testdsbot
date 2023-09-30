import discord
from bot_logic import gen_pass
from bot_logic import toss_coin

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$genpass'):

        len = int(message.content.split()[1])
        ps = gen_pass(len)
        await message.channel.send(ps)

    elif message.content.startswith('$tosscoin'):
        await message.channel.send(toss_coin())

    elif message.content.startswith('$hello'):
        await message.channel.send("Hi!")

    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")

    else:
        await message.channel.send(message.content)

client.run("MTE1NTE2NzA1OTY0NzQwNjA4MA.GMbA-9.Jwlh8Ko-WUy0s_IzX1FBoDOzHAbJabWyyMw8xQ")