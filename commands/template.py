import discord
from discord.ext import commands

class Template(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs Loaded')

    #Commands

def setup(bot):
    bot.add_cog(Template(bot))
