import discord
import random
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

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

bot.run("ну типо код ляляля")
