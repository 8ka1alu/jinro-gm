import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jmeduim(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='霊媒')
    async def meduim(self, ctx):
        return

def setup(bot):
    bot.add_cog(jmeduim(bot))
