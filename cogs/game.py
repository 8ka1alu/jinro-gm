import os
import r
from discord.ext import commands
import random

class jgame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def start(self, ctx):
        """開始"""
        conn=r.connect()
        d=conn.smembers("人狼参加者")
        dd=[j for j in d]
        if "0" not in dd:
            await ctx.send('現在使用できません')
        else:
            pp=conn.srem("人狼参加者","0")


    @commands.command()
    async def end(self, ctx):
        """強制終了"""
        conn=r.connect()
        d=conn.smembers("人狼参加者")
        dd=[j for j in d]
        if "0" not in dd:
            await ctx.send("強制終了します")
            pp=conn.sadd("人狼参加者","0")
            await ctx.send(pp)
        else:
            await ctx.send("現在使用できません")
        
    @commands.command()
    async def logout(self, ctx):
        """再起動"""
        await ctx.send('再起動します')
        conn=r.connect()
        d=conn.smembers("人狼参加者")
        dd=[j for j in d]
        if "0" not in dd:
            p=conn.sadd("人狼参加者","0")
        await self.bot.logout()

def setup(bot):
    bot.add_cog(jgame(bot))