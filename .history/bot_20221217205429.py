import discord
from discord.ext import commands
import json
import os

with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Loaded {extension} done...')

@bot.command()
async def unload(ctx, extension):
    bot.unload_extensionload_extension(f'cmds.{extension}')
    await ctx.send(f'Unloaded {extension} done...')

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reloaded {extension} done...')

for filename in os.listdir("./cmds"):
    if filename.endswith('.py'):
        bot.load_extension(f"cmds.{filename[:-3]}")
        print(f'Loaded {filename}.')
print('Done.')

if __name__ == "__main__":
    bot.run(jdata['TOKEN'])
