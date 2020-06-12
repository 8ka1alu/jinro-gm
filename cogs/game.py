import os
import r
from discord.ext import commands
import discord
import random
import asyncio

class jgame(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def end(self, ctx):
        """強制終了"""
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
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
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
        await ctx.send('再起動します')
        await self.bot.change_presence(status=discord.Status.dnd,activity=discord.Game(name=f'再起動'))
        d=conn.delete("人狼参加者")
        await asyncio.sleep(5)
        p=conn.sadd("人狼参加者","0")
        await self.bot.logout()

    @commands.command()
    async def start(self, ctx):
        """開始"""
        conn=r.connect()
        kk=conn.smembers("開発管理者")
        k=[l for l in kk]
        cai=ctx.author.id
        cai=str(cai)
        if cai not in k:
            return await ctx.send("使用できません")
        d=conn.smembers("人狼参加者")
        dd=[j for j in d]
        if "0" not in dd:
            await ctx.send('現在使用できません')
        else:
            if len(d)==1:
                return await ctx.send("参加者が足りません")
            pp=conn.srem("人狼参加者","0")
            await ctx.send("ゲームを開始します")


def setup(bot):
    bot.add_cog(jgame(bot))
