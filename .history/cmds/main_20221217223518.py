from discord.ext import commands
from core.classesclasses import Cog_Extension
from requests import get
import discord
import json


with open("setting.json", mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000)}(ms)')

    @commands.command()
    async def serverIP(self, ctx):
        IP = get(jdata['https://api.ipify.org']).content.decode('utf8')
        await ctx.send(f'Server IP:{IP}')

async def setup(bot):
    await bot.add_cog(Main(bot))