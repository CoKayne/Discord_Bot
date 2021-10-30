from typing import AsyncGenerator
import discord
import json
import random
from discord import channel
from emoji import emojize
from discord.ext import commands
intents = discord.Intents.all()
from core.classes import Cog_extension

with open("setting.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

class Event(Cog_extension): #just testing

    @commands.Cog.listener() #welcome message send to sever
    async def on_member_join(self, member):
        channel = self.bot.get_channel(int(jdata["HELLO"]))
        embed=discord.Embed(color=0xf0ac19)
        stringa = str(f">>>>>{member.mention}<<<<<")
        embed.add_field(name=("----- 歡迎來到建功俱樂部 -----"), value=stringa, inline=True)
        await channel.send(embed=embed)

    @commands.Cog.listener() #leave message send to sever
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(int(jdata["HELLO"]))
        embed=discord.Embed(color=0xf0ac19)
        stringa = str(f">>>>>{member.mention}<<<<<")
        embed.add_field(name=("----- 離開了建功俱樂部 -----"), value=stringa, inline=True)
        await channel.send(embed=embed)

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
        if data.message_id == 903887536215179295:
            guild = self.bot.get_guild(data.guild_id)
            if str(data.emoji) == u"\U0001F550": #501
                role = guild.get_role(903657203062415380)    
            if str(data.emoji) == u'\U0001f551': #502
                role = guild.get_role(903667971757576193)
            if str(data.emoji) == u'\U0001f552': #503
                role = guild.get_role(903668063331840040)
            if str(data.emoji) == u'\U0001f553': #504
                role = guild.get_role(903666784937332838)
            if str(data.emoji) == u'\U0001f554': #505
                role = guild.get_role(903667756963086417)
            if str(data.emoji) == u'\U0001f555': #506
                role = guild.get_role(903667862152032316)
            if str(data.emoji) == u'\U0001f556': #507
                role = guild.get_role(903668157439434802)
            if str(data.emoji) == u'\U0001f557': #508
                role = guild.get_role(903668182416494644)
            await data.member.add_roles(role)            
            await data.member.send(f"恭喜你成為 {role} 的一員 !")

    @commands.Cog.listener() #emoji remove roles + DM
    async def on_raw_reaction_remove(self, data):
        if data.message_id == 903887536215179295:
            guild = self.bot.get_guild(data.guild_id)
            user = guild.get_member(data.user_id)
            if str(data.emoji) == u"\U0001F550": #501
                role = guild.get_role(903657203062415380)    
            if str(data.emoji) == u'\U0001f551': #502
                role = guild.get_role(903667971757576193)
            if str(data.emoji) == u'\U0001f552': #503
                role = guild.get_role(903668063331840040)
            if str(data.emoji) == u'\U0001f553': #504
                role = guild.get_role(903666784937332838)
            if str(data.emoji) == u'\U0001f554': #505
                role = guild.get_role(903667756963086417)
            if str(data.emoji) == u'\U0001f555': #506
                role = guild.get_role(903667862152032316)
            if str(data.emoji) == u'\U0001f556': #507
                role = guild.get_role(903668157439434802)
            if str(data.emoji) == u'\U0001f557': #508
                role = guild.get_role(903668182416494644) 
            await user.remove_roles(role)            
            await user.send(f"你目前已不是 {role} 的一員了 !")
    
    @commands.Cog.listener()
    async def on_message_delete(self, msg):
        pass

def setup(bot):
    bot.add_cog(Event(bot))