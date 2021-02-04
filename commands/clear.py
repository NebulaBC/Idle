import discord
from discord.ext import commands

class Clear(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command()
    async def clear(self, ctx, amount=6):
        await ctx.channel.purge(limit=amount + 1)

def setup(bot):
    bot.add_cog(Clear(bot))
