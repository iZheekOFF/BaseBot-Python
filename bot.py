import discord
from discord.ext import commands

client = commands.Bot(command_prefix = 'prefix de tu bot')

@client.event
async def on_ready():
  print(f'Bot listo!')

client.run('token de tu bot')