import os
import random

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

def readfile(filename) :
    with open(filename) as file_object:
        contents = file_object.read()
    return contents

@bot.command(name="99", help = readfile('99help.txt') )
async def nine_nine(ctx, keyw) :
    
    brooklyn_99_quotes = {
        "100" : 'I\'m the human form of the 💯 emoji.',
        "bp" : "Bingpot!",
        "cool" : (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
        'adr' : 'With all due respect, I am gonna completely ignore everything you just said.',
        'el' : ('The English language can not fully capture the depth and complexity of '
        'my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face.'
        ),
        'rt' : 'Jake, why don’t you just do the right thing and jump out of a window?',
        'title' : 'Title of your sex tape.'
    }

    for key, value in brooklyn_99_quotes.items() :
        if keyw == key :
            await ctx.send(value)
    
@bot.command(name='roll', help = readfile('rollhelp.txt'))
async def roll(ctx, no_of_dice: int, no_of_sides: int) :
    dice = [
        str(random.choice(range(1, no_of_sides+1 ))) for _ in range(no_of_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)