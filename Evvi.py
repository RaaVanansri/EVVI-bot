import os
import discord
import requests
import json
import pymongo
from dotenv import load_dotenv
load_dotenv()

#client = commands.Bot(command_prefix="/", case_insensitive=True)

client = discord.Client()
evvi = os.getenv('TOKEN')
ella = os.getenv('FILTH')
el = os.getenv('RAAVANAN')
db = pymongo.MongoClient("mongodb://raavanan:Sr1kutty77@cluster0-shard-00-00.z89ji.mongodb.net:27017,cluster0-shard-00-01.z89ji.mongodb.net:27017,cluster0-shard-00-02.z89ji.mongodb.net:27017/Channel?ssl=true&replicaSet=atlas-5yhivq-shard-0&authSource=admin&retryWrites=true&w=majority")

vardb = db["Channel"]
c_id = vardb["channel_id"]
bcid = {"bumpcid":0}

x = c_id.insert_one(bcid)

print(bcid)

def bumpchannel(cid):
  bcid_update = {"bumpcid":cid}
  x = c_id.update_one(bcid,bcid_update)


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
      await message.delete()
      await client.process_commands(message)

  if message.content.startswith('/filth'):
    if message.author.id == el:
      await message.channel.send(f'Hey <@{ella}>, <@{el}> asking for hugs')
    else:
      await message.channel.send('Sorry fella, only raavanan can use this command')

  if message.content.startswith('/raavanan'):
    if message.author.id == ella:
      await message.channel.send(f'Hey <@{el}>, your gorl <@{ella}> asking for hugs you slug')
    else:
      await message.channel.send('Sorry fella, only filth can use this command')

  if message.content.startswith('/set auto bump'): 
    b1cid = {"bumpcid": message.channel.id}
    x = c_id.update_one({'_id': '624288e2c9fced7e94938ae4'},{"$set": {"bumpcid":message.channel.id}}, upsert=True)


client.run(evvi)