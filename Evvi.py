import os
import discord
import requests
import json
from dotenv import load_dotenv
load_dotenv()

#client = commands.Bot(command_prefix="/", case_insensitive=True)

client = discord.Client()
my_secret = os.getenv('TOKEN')

def get_quote():
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Reporting Duty {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')
  if message.content.startswith('/quote'):
    quote1 = get_quote()
    await message.channel.send(quote1)

@client.event
async def on_message(message):
  if "otha" in message.content:
    #user = message.content.get.user()
          #print("Something")
          #or
    await message.channel.send("Aabasam thaveerpom friends")
    await client.process_commands(message)

client.run(my_secret)