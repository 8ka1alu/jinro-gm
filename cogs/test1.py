import os
import r
from discord.ext import commands

class jinro(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(jinro(bot))
