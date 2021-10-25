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

class Event(Cog_extension):

    @commands.Cog.listener() #welcome message send to sever
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["HELLO"]))
        await channel.send(F"{member} joins!")

    @commands.Cog.listener() #leave message send to sever
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["HELLO"]))
        await channel.send(F"{member} leave!")

    @commands.Cog.listener() #active keyword bot send me
    async def on_message(self, msg):
        if msg.content in jdata["KEYWORD"] and msg.author != self.bot.user:
            await msg.channel.send("hi")
        pic = discord.File("C:\\Users\\Kayne\\Desktop\\Discord_Bot\\cmds\\cool_pictures\\2021-09-26_1.27.46.png")
        if msg.content.endswith("JACK"):
            await msg.channel.send(file = pic)

    @commands.Cog.listener() #error response
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send("Missing arguments!")
        elif isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("There is no such command!")
        else:
            await ctx.send("An error occured")
       
    @commands.Cog.listener() #emoji add roles + DM
    async def on_raw_reaction_add(self, data): 
        if data.message_id == 901404123998609440:
            if str(data.emoji) == u"\u26D4":
                guild = self.bot.get_guild(data.guild_id)
                role = guild.get_role(901110622664679485)
                await data.member.add_roles(role)            
                await data.member.send(f"You have become {role}!")

    @commands.Cog.listener() #emoji remove roles + DM
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 901404123998609440:
            if str(data.emoji) == u"\u26D4":
                guild = self.bot.get_guild(data.guild_id)
                user = guild.get_member(data.user_id)
                role = guild.get_role(901110622664679485)
                await user.remove_roles(role)            
                await user.send(f"You are not {role} any more!")
    
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        pass

def setup(bot):
    bot.add_cog(Event(bot))