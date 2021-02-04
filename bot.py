import discord
from discord.ext.commands import Bot
#from dotenv import load_dotenv
#import os

#load_dotenv(.env)

intents = discord.Intents.default()
intents.members = True

bot = Bot(">", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} is ready.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(len(bot.guilds)) + " servers"))

@bot.event
async def on_member_join(member):
    await member.send('Welcome to the server!')
    print (f'{member} has joined the server')

@bot.event
async def on_member_remove(member):
    print (f'{member} has left the server')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong')

bot.run('')
#client.run(os.getenv('IDLE_BOT_TOKEN'))
