import discord
from discord.ext.commands import Bot

class Template(commands.Cog):

    def __init__(self, bot):
        self.bot = client

    #Events
    @commands.Cog.listener
    async def on_ready(self):
        print('Cogs Loaded')

    #Commands
    @commands.command()
    async def template(self, ctx):
        await ctx.send('Cogs Currently Enabled')

def setup(bot):
    bot.add_cog(Template(bot))
