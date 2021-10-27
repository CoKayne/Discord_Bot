from typing import AsyncGenerator
import discord
import json
import random
import datetime
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()
from core.classes import Cog_extension

with open("setting.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class Main(Cog_extension):

    @commands.command() #show now ping (ms)
    async def ping(self, ctx):
        await ctx.send(F"{round(self.bot.latency * 1000)} (ms)")

    @commands.command() #send ABCD message
    async def hi(self, ctx):
        await ctx.send("ABCD")

    @commands.command() #bot embed
    async def embed(self, ctx):
        embed=discord.Embed(title="About", url="https://www.youtube.com/watch?v=ZZ5LpwO-An4", 
        description="this is my description", color=0xf0ac19, timestamp = datetime.datetime.utcnow())
        embed.set_author(name="HEYYEYAAEYAAAEYAEYAA", url="https://www.youtube.com/watch?v=ZZ5LpwO-An4", icon_url="https://i.kym-cdn.com/entries/icons/original/000/002/691/sings.jpg")
        embed.set_thumbnail(url="https://i.kym-cdn.com/entries/icons/original/000/002/691/sings.jpg")
        embed.add_field(name="I said hey", value="What's going on??", inline=False)
        embed.add_field(name=":)", value="Not much. brb.", inline=False)
        embed.set_footer(text="189,382,718")
        await ctx.send(embed=embed)

    @commands.command() #bot say message
    async def said(self, ctx, *,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command() #clean message 
    async def clean(self, ctx, num : int):
        await ctx.channel.purge(limit = num+1)
    
    @commands.command() #online random squad
    async def rand_squad(self, ctx):
        online = []
        for member in ctx.guild.members:
            if str(member.status) == "online" and member.bot == False:
                online.append(member.name)

        random_online = random.sample(online, k = 1) #幾個人分組

        for squad in range(1): #分幾組
            a = random.sample(random_online, k = 1) #一組幾個人
            nonochars = "[]'" #去掉的chars
            stringa = str(a)  #str(a)
            for chars in nonochars:
                stringa = stringa.replace(chars,"")
            embed=discord.Embed(title="分組", description="各組分組結果", color=0xf0ac19)
            embed.add_field(name=(f"Group {squad+1} "), value=stringa, inline=False)
            await ctx.send(embed=embed) #輸出
            for name in a:
                random_online.remove(name) #不要重複選
    
    @commands.command() #class_squad
    async def class_squad(self, ctx):
        people = jdata["CSDC"]
        backup = [] 
        for squad in range(8):
            a = random.sample(people, k=3)
            nonochars = "[]'" #去掉的chars
            stringa = str(a)  #str(a)
            for chars in nonochars:
                stringa = stringa.replace(chars,"")
            embed=discord.Embed(color=0xf0ac19)
            embed.add_field(name=(f"Group {squad+1} "), value=stringa, inline=False)
            await ctx.send(embed=embed) #輸出
            for name in a:
                people.remove(name) #不要重複選
                backup.append(name)
        people.extend(backup)

    @commands.group()
    async def codetest(self, ctx):
        pass

    @codetest.command()
    async def python(self, ctx):
        await ctx.send("python")

    @codetest.command()
    async def cpp(self, ctx):
        await ctx.send("C++")
    
    @codetest.command()
    async def java(self, ctx):
        await ctx.send("java")


def setup(bot):
    bot.add_cog(Main(bot))