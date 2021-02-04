import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
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
#    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(len(bot.guilds)) + " servers | >help"))
    bot.loop.create_task(status_task())

@bot.event
async def status_task():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(len(bot.guilds)) + " servers"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= ">help for commands"))
        await asyncio.sleep(10)

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
    embedVar.add_field(name=">clear <amount>", value="Clear messages from a channel", inline=False)
    embedVar.add_field(name=">kick <@member> <Reason>", value="Kick a member from the discord server", inline=False)
    embedVar.add_field(name=">ban <@member> <Reason>", value="Ban a member from the discord server", inline=False)
    await ctx.send(embed=embedVar)

@bot.command()
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount + 1)

@bot.command()
@has_permissions(manage_roles=True, kick_members=True)
async def kick(ctx, user: discord.Member):
    await ctx.send(f'{user.name} Has Been Kicked!')
    await ctx.guild.kick(user)

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)

@bot.command()
@has_permissions(manage_roles=True, kick_members=True)
async def ban(ctx, user: discord.Member):
    await ctx.send(f'{user.name} Has Been Banished!')
    await ctx.guild.ban(user)

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, MissingPermissions):
        text = "Sorry {}, you do not have permissions to do that!".format(ctx.message.author)
        await ctx.send(text)

bot.run('')
#client.run(os.getenv('IDLE_BOT_TOKEN'))
