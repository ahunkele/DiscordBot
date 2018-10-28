import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from threading import Event

TOKEN = 'NTA1NDAwMDgzNzg1OTczNzYw.DrTF_g.V4uLjd1q1KWqq_uTPmcE2rwZvk8'
bot = commands.Bot(command_prefix='B==D ')
exit = Event()
mute_list = []


@bot.event
async def on_ready():
    print('ready')

async def do_it(): 
    await bot.server_voice_state(mute_list[0], mute=True, deafen=True)
    
@bot.command(pass_context=True)
@commands.has_role("MatthewMuteRole")
async def cuck_matthew(ctx):
    await bot.say('starting matthew mute watch')
    while not exit.is_set():
        await do_it()
        exit.wait(1)

@bot.command(pass_context=True)
@commands.has_role("MatthewMuteRole")
async def mute(ctx, member: discord.Member):
    if(len(mute_list) > 0):
        mute_list[0] = member
    else:
        mute_list.append(member)

@bot.command(pass_context=True)
@commands.has_role("MatthewMuteRole")
async def stop():
    mute_list.clear
    exit.set()
    await bot.say('_\'\'\'U luky kid. I stop. for now\'\'\'_ ')
    exit.clear()

@bot.command(pass_context=True)
async def commands():
    await bot.say("set target to mute with the B==D mute @member command")
    await bot.say("then run the B==D cuck_matthew command to start the muting/defaning")
    await bot.say("B==D stop to stop the process. May take a few seconds to go through.")

bot.run(TOKEN)
