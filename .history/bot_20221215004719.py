import discord
from discord.ext import commands
from requests import get

bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready(): 
    print("Bot is online")

@bot.command()
async def serverIP(ctx):
    IP = get('https://api.ipify.org').content.decode('utf8')
    await ctx.send(f'Sever IP:{IP}')

bot.run('MTA1MjU4ODE1ODU4OTYxNjE0OQ.GSHHb8.reUyA03sr7p3ffTnntc_pg_Uqg1oK8xDdvsN8E')
