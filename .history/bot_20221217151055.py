import discord
from discord.ext import commands
from requests import get
import json

with open("setting.json", mode = 'r', encoding = 'utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    channel = bot.get_all_channels(int(jdata['Minecraft_channel']))
    print("Bot is online")
    await

@bot.command()
async def serverIP(ctx):
    IP = get('https://api.ipify.org').content.decode('utf8')
    await ctx.send(f'Server IP:{IP}')

async def rickroll(ctx)

bot.run(jdata['TOKEN'])
