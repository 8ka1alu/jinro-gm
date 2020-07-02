import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jwerewolf(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='襲撃')
    async def werewolf(self, ctx):
        return

def setup(bot):
    bot.add_cog(jwerewolf(bot))
