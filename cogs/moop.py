import os
import sys
import discord
from discord.abc import PrivateChannel
from discord.ext import commands


class Moop(commands.Cog):
    def __init__(self, bot, dad):
        self.bot = bot
        self.dad = dad

    @commands.command()
    async def ping(self, ctx):
        """returns a 'pong' at the next available convenience"""
        await ctx.send('pong')
        return

    @commands.command()
    async def restart(self, ctx):
        """restarts moop"""
        if (ctx.message.author.id == int(dad)):
            await ctx.send('okay, restarting')
            os.system("sh $HOME/moop.sh &")
            sys.exit()
            return

    @commands.command()
    async def horseplinko(self, ctx):
        """posts horse plinko"""
        if not isinstance(ctx.channel, PrivateChannel):
            await ctx.message.delete()
            # else:
            #     await ctxt.send('fuckin cant bitch')
        await ctx.send(files=[
            discord.File('./assets/horse1.gif'),
            discord.File('./assets/horse2.gif')
        ])
        return
