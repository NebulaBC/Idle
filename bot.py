import discord
from discord.ext.commands import Bot
#from dotenv import load_dotenv
#import os

#load_dotenv(.env)

intents = discord.Intents.default()
intents.members = True

bot = Bot(">", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} is ready.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(len(bot.guilds)) + " servers | >help"))

@bot.event
async def on_member_join(member):
    await member.send(f'Welcome to {member.guild.name}!')
    print (f'{member} has joined a server')

@bot.event
async def on_member_remove(member):
    print (f'{member} has left a server')

@bot.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(bot.latency * 1000)}ms')

@bot.command()
async def help(ctx):
    embedVar = discord.Embed(title="Help", description="", color=0x3410d4)
    embedVar.add_field(name=">ping", value="Get the ping of IDLE bot", inline=False)
    embedVar.add_field(name=">kick <@member> <Reason>", value="Kick a member from the discord server", inline=False)
    embedVar.add_field(name=">ban <@member> <Reason>", value="Ban a member from the discord server", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
async def kick(ctx, user: discord.Member):
    await ctx.send(f'{user.name} Has Been Kicked!')
    await ctx.guild.kick(user)

@bot.command()
async def ban(ctx, user: discord.Member):
    await ctx.send(f'{user.name} Has Been Banished!')
    await ctx.guild.ban(user)

bot.run('')
#client.run(os.getenv('IDLE_BOT_TOKEN'))
