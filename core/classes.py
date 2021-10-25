from typing import AsyncGenerator
import discord
import json
import random
from discord import channel
from discord.ext import commands
intents = discord.Intents.all()

class Cog_extension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot