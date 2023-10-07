import discord
import random
import requests
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import toss_coin

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def genpass(ctx,pass_lenght = 8):
    await ctx.send(f'Ваш пароль: {gen_pass(pass_lenght)}')

@bot.command()
async def commands(ctx):
    await ctx.send('Существующие команды:\n'
                   '1. genpass - генерирует пароль указанной вами длины\n'
                   '2. tosscoin - подбрасывает монетку\n' 
                   '3. hello - бот представится своим именем\n'  
                   '4. heh - пишет сообщение со смехом указанной вами длины\n'
                   '5. repeat - повтоворяет ваше сообщение указанное количество раз\n'  
                   '6. mem - отправляет мемы про программирование\n'
                   '7. dog - отправляет случайное фото с собакой\n'  
                   '8. duck - отправляет случайное фото с уткой')

@bot.command()
async def tosscoin(ctx):
    await ctx.send(toss_coin())

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def mem(ctx):
    a = random.randint(1,4)
    with open(f'images/mem{a}.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def get_dog_image_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def animals(ctx):
    grade = ''
    a = random.randint(1,100)
    if 1 <= a <= 70:
        b = random.randint(1,5)
        grade = 'common'
        with open(f'animalsmemes/{grade}/mem{b}.jpg', 'rb') as f:
            picture = discord.File(f)
    elif 71 <= a <= 95:
        b = random.randint(1, 3)
        grade = 'rare'
        with open(f'animalsmemes/{grade}/mem{b}.jpg', 'rb') as f:
            picture = discord.File(f)
    elif 96 <= a <= 100:
        grade = 'legendary'
        with open(f'animalsmemes/{grade}/mem1.jpg', 'rb') as f:
            picture = discord.File(f)

    await ctx.send(file=picture)
    if grade == 'common':
        await ctx.send('Вам выпал обычный мем')
    elif grade == 'rare':
        await ctx.send('Вам выпал редкий мем')
    elif grade == 'legendary':
        await ctx.send('Вам выпал легендарный мем \nP.s: Ты везунчик)')

@bot.command('dog')
async def dog(ctx):
    '''По команде dog вызывает функцию get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

bot.run("а меня нет)")

