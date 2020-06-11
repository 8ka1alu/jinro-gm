import os
import r
from discord.ext import commands
import random

class jgame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        conn=r.connect()
        pp=conn.srem("人狼参加者","0")
        

def setup(bot):
    bot.add_cog(jgame(bot))
