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
            ky=conn.keys()
            kys=[j for j in ky]
            for b in kys:
                if b in dd:
                    du=conn.delete(b)
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
        ky=conn.keys()
        js=conn.smembers("人狼参加者")
        jss=[f for f in js]
        kys=[j for j in ky]
        for b in kys:
            if b in jss:
                du=conn.delete(b)
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
            rp=conn.smembers("人狼役職")
            rpp=[j for j in rp]
            m=1
            for i in rpp:
                dp=conn.get(i)
                m+=int(dp)
            if len(d)!=m:
                return await ctx.send("参加者もしくは役職が足りません")
            pp=conn.srem("人狼参加者","0")
            dd.remove("0")
            await ctx.send("ゲームを開始します")
            await asyncio.sleep(0.5)
            await ctx.send("0日目\n役職がDMに配布されます")
            for ro in rpp:
                qe=conn.get(ro)
                m=0
                while m<int(qe):
                    user=random.choice(dd)
                    up=self.bot.get_user(int(user))
                    await up.send(f"貴方は**{ro}**です")
                    p=conn.set(user,ro)
                    dd.remove(up)
                    m+=1

    @commands.command()
    async def say(self, ctx, *, msg:int):
        await ctx.send(msg)
        await ctx.send(len(msg))

def setup(bot):
    bot.add_cog(jgame(bot))
