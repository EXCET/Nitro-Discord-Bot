import discord 
from discord.ext import commands
import os
import time
import string
import random

token = "token here"

prefix = "!"

bot = commands.Bot(command_prefix=prefix, help_command=None)


@bot.command()
async def nitro(ctx):
  code = "".join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=16))
  nitro = f"https://discord.gift/{code}"
  embed=discord.Embed(color=0xee00ff, description=f"``🎯``**Nitro Gen**\n\n**TYPE**\n``🎁`` Nitro Boost\n\n**TIME**\n``🕛`` 47 hours left\n\n**LINK**\n``🔗`` ||{nitro}||")
  await ctx.send(embed=embed)


bot.run(token)
