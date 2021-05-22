import os
import random

import discord
from discord import channel
from discord import guild
from discord import client
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = 't ')

# utility fucn, opens and reads file contents
def readfile(filename) :
    with open(filename) as file_object:
        contents = file_object.read()
    return contents

# i am trying. to count how many monkes texted in server.
def count_monke(msg):

    cntf = 0
    msg.content = msg.content.lower()
    cntf += msg.content.count("monke")

    if cntf :
        with open('monkes.txt', 'r+') as file_object:
            cnt = int(file_object.read()) #code gets stuck here
            print(cnt)
            cnt+=cntf 
            print(cnt)
            file_object.seek(0)
            file_object.truncate()
            print("\nTruncated file.")
            file_object.write(str(cnt))
            print("\nwrote into file.")



# want the bot to say hi when it lands (as of now it just pops out a msg when it goes online)
@bot.event
async def on_ready():
    print(f'{bot.user.name} is online!')
    channel = bot.get_channel(834718249013870615)
    await channel.send("Hola amigooooooooooz I am online! ♪┏(・o･)┛♪┗ ( ･o･) ┓♪")
    await bot.change_presence(status = discord.Status.online, activity = discord.Game("ze vibes ♪┏(・o･)┛♪"))

# event that reads each message and calls count_monke() if message contains monke
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    elif message.content.lower().count("monke") == 0 :
        return
    count_monke(message)
    print("\nRead message.")
    await bot.process_commands(message)

# command to display no. of monkez ToT
@bot.command(name="monke", help = "counts monkes")
async def monke_count(ctx) :
    with open('monkes.txt') as file_object:
        cnt = file_object.read()
        print("\ncnt read from file before sending it to channel = " + cnt)
        await ctx.send(cnt)
        file_object.close()


# command that displays b99 quotes
@bot.command(name="99", help = readfile('99help.txt') )
async def nine_nine(ctx, keyw, err) :
    
    if err == "on_command_error":
        await ctx.send("Typethe appropriate keyword! Or type t help 99 for help.")

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


# command to roll a dice but i'm removing this soon
@bot.command(name='roll', help = readfile('rollhelp.txt'))
async def roll(ctx, no_of_dice: int, no_of_sides: int) :
    dice = [
        str(random.choice(range(1, no_of_sides+1 ))) for _ in range(no_of_dice)
    ]
    await ctx.send(', '.join(dice))

# count monke command
@bot.command(name="monke", help = "counts monkes")
async def monke_count(ctx) :
    with open('monkes.txt') as file_object:
        cnt = file_object.read()
        print("\ncnt read from file before sending it to channel = " + cnt)
        await ctx.send(cnt)
        file_object.close()

# @bot.command()
# async def ping

bot.run(TOKEN)
