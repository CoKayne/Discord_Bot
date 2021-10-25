from typing import AsyncGenerator
import discord
import json
import random
import datetime
import asyncio
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()
from core.classes import Cog_extension

class Task(Cog_extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.counter = 0

        # async def interval():
        #     await self.bot.wait_until_ready()
        #     self.channel = self.bot.get_channel(892427192871559199)
        #     while not self.bot.is_closed():
        #         await self.channel.send("hi low")
        #         await asyncio.sleep(5)
        
        # self.bg_task = self.bot.loop.create_task(interval())

        async def time_task(): #send message on a specific
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(892427192871559199)
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime("%H:%M")
                with open("setting.json", "r", encoding="utf8") as jfile:
                    jdata = json.load(jfile)
                if now_time == jdata["TIME"] and self.counter == 0:
                    await self.channel.send("Task is working!")
                    self.counter = 1
                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass
        
        self.bg_task = self.bot.loop.create_task(time_task())

    @commands.command() #set a channel to send time_task()
    async def set_channel(self, ctx, ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"set channel: {self.channel.mention}")

    @commands.command() #set a specific time
    async def set_time(self, ctx, time):
        self.counter = 0
        with open("setting.json", "r", encoding="utf8") as jfile:
            jdata = json.load(jfile)    
        jdata["TIME"] = time
        with open("setting.json", "w", encoding="utf8") as jfile:
            json.dump(jdata, jfile, indent=4)    

def setup(bot):
    bot.add_cog(Task(bot))