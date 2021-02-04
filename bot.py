import discord
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv('.env')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(command_prefix='>', intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is ready.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= str(len(client.guilds)) + " servers"))

@client.event
async def on_member_join(member):
    await member.send('Welcome to the server!')
    print (f'{member} has joined the server')

@client.event
async def on_member_remove(member):
    print (f'{member} has left the server')

@client.command()
async def ping(ctx):
    await ctx.send('Pong')

client.run(os.getenv('IDLE_BOT_TOKEN'))
