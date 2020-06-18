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
        rp2=[j for j in rp]
        if "0" not in rp2:
            return await ctx.send("既にゲームが始まっています")
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
        rp2=[j for j in rp]
        if "0" not in rp2:
            return await ctx.send("既にゲームが始まっています")
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

    @commands.command(name='参加者確認')
    async def _player(self, ctx):
        """確認"""
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
        pp=conn.smembers("人狼参加者")
        p=[j for j in pp]
        p.remove("0")
        m=1
        embed=discord.Embed(title="参加者一覧",description=None)
        for i in p:
            player=self.bot.get_user(int(i))
            embed.add_field(name=f'**{m}人目**',value=f'`{player}`')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(jinro(bot))
