import discord
import asyncio
import os
#from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions

#load_dotenv(.env)

intents = discord.Intents.default()
intents.members = True

bot = Bot(">", intents=intents, case_insensitive=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f'{bot.user} is ready.')
    bot.loop.create_task(status_task())
for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

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
