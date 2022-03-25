import os
import discord
from dotenv import load_dotenv
load_dotenv()

client = discord.Client()
my_secret = os.getenv('TOKEN')
print(my_secret)
print(type(my_secret))

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('-hello'):
    await message.channel.send('Hello!')
    
client.run(my_secret)