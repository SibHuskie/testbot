import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import os.path
import requests
import json
import time
from gtts import gTTS
import urbandictionary as ud

Client = discord.Client()
bot_prefix= "v!"
client = commands.Bot(command_prefix=bot_prefix)

@bot.command(pass_context=True)
async def messageAll(ctx):
    for server in bot.servers:
        for member in server.members:
            await bot.send_message(member, "Hello User!")

##################################
client.run(os.environ['BOT_TOKEN'])
