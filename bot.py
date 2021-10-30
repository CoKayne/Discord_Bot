from typing import AsyncGenerator
import discord
import json
import random
import os
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()

with open("setting.json", "r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix="-", intents = intents)

class MyHelpCommand(commands.MinimalHelpCommand): #make help embed
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(color=0xf0ac19, description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)
bot.help_command = MyHelpCommand()

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(F"cmds.{extension}")
    await ctx.send(F"Loaded {extension} done.")

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(F"cmds.{extension}")
    await ctx.send(F"Unloaded {extension} done.")

@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(F"cmds.{extension}")
    await ctx.send(F"Reloaded {extension} done.")

for Filename in os.listdir("./cmds"):
    if Filename.endswith(".py"):
        bot.load_extension(F"cmds.{Filename[:-3]}")

if __name__ == "__main__":
    bot.run(jdata["TOKEN"])