import os
import r
from discord.ext import commands

class jinro(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"pong! \n`{self.bot.ws.latency * 1000:.0f}ms`")

    @commands.command(name="参加")
    async def _add(self, ctx):
        conn=r.connect()
        rp=conn.smembers("人狼参加者")
        pc=0
        for rpp in rp:
            rpp=int(rpp)
            if rpp == ctx.author.id:
                pc=1
        if pc==0:
            p=conn.sadd("人狼参加者",ctx.author.id)
            if p==True:
                await ctx.send("参加登録しました！")
            else:
                await ctx.send("登録に失敗しました")
        else:
            await ctx.send("既に登録されています")

    @commands.command(name="削除")
    async def _remove(self, ctx):
        conn=r.connect()
        rp=conn.smembers("人狼参加者")
        pc=0
        for rpp in rp:
            rpp=int(rpp)
            if rpp == ctx.author.id:
                pc=1
        if pc==1:
            p=conn.srem("人狼参加者",ctx.author.id)
            if p==True:
                await ctx.send("参加削除しました！")
            else:
                await ctx.send("削除に失敗しました")
        else:
            await ctx.send("参加していません")

def setup(bot):
    bot.add_cog(jinro(bot))
