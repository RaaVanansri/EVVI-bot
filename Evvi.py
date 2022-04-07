from dis import disco
import json
import discord
import os
from pydoc import cli
import requests
from discord import Intents
import pymongo
from unique_id import get_unique_id
from discord.ext import commands
from dotenv import load_dotenv
import music

cogs = [music]

load_dotenv()
bot = commands.Bot(command_prefix="/")

evvi = os.getenv('TOKEN')
ella = os.getenv('mine')
el = os.getenv('me')
db = pymongo.MongoClient('mongodb://raavanan:Sr1kutty77@cluster0-shard-00-00.z89ji.mongodb.net:27017,cluster0-shard-00-01.z89ji.mongodb.net:27017,cluster0-shard-00-02.z89ji.mongodb.net:27017/Channel?ssl=true&replicaSet=atlas-5yhivq-shard-0&authSource=admin&retryWrites=true&w=majority')

#client = discord.Client()

for i in range(len(cogs)):
  cogs[i].setup(bot)

hel ="""
```
/hello: greetings
/quote: fetch some quotes for you
/complaint: to raise your complaint to admins
/playit<song name or link>: play songs in vc
/pause: pause the current song
/resume: resume the current song
/disconnect: disconnect from the vc
```
"""

vardb = db["Channel"]
c_id = vardb["channel_id"]
badword = vardb["badword"]
roleid = vardb["role_id"]

@bot.event
async def on_message(message):

  aabasam = ['otha','gomma','punda','thevadeya','sunni','junni','thayoli','koothi','fuck','bitch','brats','bastard']
  
  for x in aabasam:
    if x in message.content.lower():
      await message.delete()
      await message.channel.send(f"Aabasam thaveerpom friends,  <@{message.author.id}>", delete_after=7.0)

  if message.author.id == 302050872383242240 :
    
    cbchannel = c_id.find({})
    bumpc = roleid.find({})
    bumpchannel = bot.get_channel(cbchannel[2]['bumpreminder'])
    if message.channel.id == bumpchannel.id:
      bumpro = bumpc[0]['bumprole']
      await bumpchannel.send(f'It\'s Bump time bois and gorls {bumpro}')

  await bot.process_commands(message)

@bot.command()
async def hello(ctx):
  await ctx.reply('Hello!')

@bot.command()
async def complaint(ctx):
  ticket_id = get_unique_id(length=6)
  complaint_txt = ctx.message.content[11:]
  cbchannel = c_id.find({})
  cboxchannel = bot.get_channel(cbchannel[0]['cbox'])
  boxchannel = bot.get_channel(cbchannel[1]['box'])
  if cboxchannel.id == ctx.channel.id:
    await boxchannel.send(f'Ticket number:{ticket_id} \n Complaint raised by <@{ctx.author.id}> \n {complaint_txt}')
    await ctx.message.delete()
  else:
    await ctx.channel.send(f'Please send your complaint in <#{cboxchannel.id}>', delete_after=7.0)
    await ctx.message.delete()

@bot.command()
async def quote(ctx):
  response = requests.get('https://zenquotes.io/api/random')
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  await ctx.send(quote)

@bot.command()
async def setbox(ctx):
  x = c_id.update_one({'_id': 'box'},{"$set": {"box":ctx.channel.id}}, upsert=True)
  await ctx.send(f"Done. <#{ctx.channel.id}> channel is set for receiving complaints")

@bot.command()
async def setbump(ctx):
  bumprole = ctx.message.content[9:]
  roleid.update_one({'_id': 'bumprole'},{"$set": {"bumprole":bumprole}}, upsert=True)
  x = c_id.update_one({'_id': 'bumpremc'},{"$set": {"bumpreminder":ctx.channel.id}}, upsert=True)
  await ctx.send(f"Done. <#{ctx.channel.id}> channel is set for bump remainder")

@bot.command()
async def helps(ctx):
  await ctx.send(f'{hel}')
  
@bot.command()
async def setcbox(ctx):
    x = c_id.update_one({'_id': 'complaint_box'},{"$set": {"cbox":ctx.channel.id}}, upsert=True)
    await ctx.channel.send(f"Done. <#{ctx.channel.id}> channel is set for Complaint \n Use /complaint <your complaint> command")

@bot.command()
async def filth(ctx):
  if ctx.author.id == int(el):
    await ctx.send(f'Hey <@{ella}>, <@{el}> asking for hugs')
  else:
    await ctx.send('Sorry fella, only raavanan can use this command')
  
@bot.command()
async def raavanan(ctx):
  if ctx.author.id == int(ella):
    await ctx.send(f'Hey <@{el}>, <@{ella}> asking for hugs')
  else:
    await ctx.send('Sorry fella, only filth can use this command')

bot.run(evvi)