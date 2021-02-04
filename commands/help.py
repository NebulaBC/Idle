import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #Commands
    @commands.command()
    async def help(self, ctx):
        embedVar = discord.Embed(title="Help", description="", color=0x3410d4)
        embedVar.add_field(name=">ping", value="Get the ping of IDLE bot", inline=False)
        embedVar.add_field(name=">clear <amount>", value="Clear messages from a channel", inline=False)
        embedVar.add_field(name=">kick <@member> <Reason>", value="Kick a member from the discord server", inline=False)
        embedVar.add_field(name=">ban <@member> <Reason>", value="Ban a member from the discord server", inline=False)
        emoji = '\N{CLOSED MAILBOX WITH RAISED FLAG}'
        await ctx.message.add_reaction(emoji)
        await ctx.author.send(embed=embedVar)

def setup(bot):
    bot.add_cog(Help(bot))
