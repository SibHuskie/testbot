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

@client.command(pass_context = True)
async def dm(ctx, member : discord.Member = None, *, message):
    if not ctx.message.author.server_permissions.administrator:
        return
    if not member:
        return await client.say(ctx.message.author.mention + "Specify a user to DM!")
    if member == "@everyone":
    for server_member in ctx.message.server.members:
        await client.send_message(server_member, message)

##################################
client.run(os.environ['BOT_TOKEN'])
