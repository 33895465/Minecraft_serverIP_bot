from discord.ext import commands
from dotenv import load_dotenv
from os import listdir, getenv
import discord
import asyncio
import json

load_dotenv()
TOKEN = getenv('TOKEN')

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.event
async def on_ready():
    # channel = bot.get_all_channels(int(jdata['Minecraft_channel']))
    print("Bot is online")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done...')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done...')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done...')

async def load_extensions():
    for filename in listdir("./cmds"):
        if filename.endswith('.py'):
            await bot.load_extension(f"cmds.{filename[:-3]}")
            print(f'Loaded {filename}.')

async def main():
    async with bot:
        await load_extensions()
        await bot.start(jdata['TOKEN'])
        # await bot.run(jdata['TOKEN'])

asyncio.run(main())

# if __name__ == "__main__":
#     bot.run(jdata['TOKEN'])