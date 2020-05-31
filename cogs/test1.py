import os
import r
from discord.ext import commands

class jinro(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong! \n`{self.bot.ws.latency * 1000:.0f}ms`")

def setup(bot):
    bot.add_cog(jinro(bot))
