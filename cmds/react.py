from typing import AsyncGenerator
import discord
import json
import random
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()
from core.classes import Cog_extension

with open("setting.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class React(Cog_extension):

    @commands.command() #send pictures on my computer
    async def pics(self, ctx):
        random_pic = random.choice(jdata["pic"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    @commands.command() #send pictures online
    async def webpic(self, ctx):
        random_pic = random.choice(jdata["url_pic"])
        await ctx.send(random_pic)

    @commands.command()
    async def speak(self, ctx):
        role = ctx.guild.get_role(901110622664679485)
        rlist = role.members
        for name in rlist:
            await name.send("Go eat")
            await ctx.send(name)

    @commands.command()
    async def div(self, ctx):
        divider = str(jdata["DIVIDER"])
        await ctx.send(divider[2:79])

def setup(bot):
    bot.add_cog(React(bot))