import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jfortune(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='占い')
    async def fortune(self, ctx):
        return

def setup(bot):
    bot.add_cog(jfortune(bot))
