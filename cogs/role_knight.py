import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jknight(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='守り')
    async def knight(self, ctx):
        return

def setup(bot):
    bot.add_cog(jknight(bot))
