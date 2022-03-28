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

  aabasam = ['otha','gomma','punda','thevadeya','sunni','junni','thayoli','koothi']
  
  if message.author == client.user:
    return

  if message.content.startswith('/hello'):
    await message.channel.send('Hello!')
    
  if message.content.startswith('/quote'):
    quote1 = get_quote()
    await message.channel.send(quote1)

  for x in aabasam:
    if x in message.content:
      #user = message.content.get.user()
            #print("Something")
            #or
      await message.channel.send(f"Aabasam thaveerpom friends,  <@{message.author.id}>")
      await client.process_commands(message)

  if message.content.startswith('/filth'):
    if message.author.id == 861169200968892417:
      await message.channel.send(f'Hey <@{929079385737281586}>, <@{861169200968892417}> asking for hugs')
    else:
      await message.channel.send('Sorry fella, only raavanan can use this command')

  if message.content.startswith('/raavanan'):
    if message.author.id == 929079385737281586:
      await message.channel.send(f'Hey <@{861169200968892417}>, your gorl <@{929079385737281586}> asking for hugs you slug')
    else:
      await message.channel.send('Sorry fella, only filth can use this command')

client.run(my_secret)