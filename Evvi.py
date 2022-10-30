import json
import os
from random import randint
from aiohttp import payload_type
import requests
import pymongo
import discord
from setuptools import Command
from unique_id import get_unique_id
from discord.ext import commands
from dotenv import load_dotenv
import music

cogs = [music]

load_dotenv()
bot = commands.Bot(command_prefix="!")

# currencycon_data = {'format':'json', 'api_key':'[YOUR_API_KEY]','from':'USD','to':'EUR','amount':'120'}
# response = requests.post('https://api.iban.com/clients/api/currency/convert/',currencycon_data)
# print(response.text)

evvi = os.getenv('TOKEN')
ella = os.getenv('mine')
el = os.getenv('me')
connectionstring = os.getenv('DBCONSTR')
db = pymongo.MongoClient(connectionstring)
print(db)
#client = discord.Client()

for i in range(len(cogs)):
  cogs[i].setup(bot)

hel ="""
```
!hello                          : greetings
!quote                          : fetch some quotes for you
!complaint                      : to raise your complaint
!q                              : Ask questions and get reply (not like chat but pretty much 8 Ball)
!htd                            : Converts Hexa decimal to Decimal
!play or !p <song name or link> : play songs in vc
!pause or !pa                   : pause the current song
!resume or !res                 : resume the current song
!disconnect or !dc              : disconnect from the vc
```
"""

vardb = db["Channel"]
c_id = vardb["channel_id"]
badword = vardb["badword"]
roleid = vardb["role_id"]

bot.remove_command('help')

@bot.event
async def on_message(message):
  aabasam = ['fuck','bitch','brats','bastard']
  for x in aabasam:
    if x in message.content.lower():
      await message.delete()
      await message.channel.send(f"Aabasam thaveerpom friends,  <@{message.author.id}>", delete_after=7.0)
  # if message.author.id == 302050872383242240 :
  #   cbchannel = c_id.find({})
  #   bumpc = roleid.find({})
  #   bumpchannel = bot.get_channel(cbchannel[2]['bumpreminder'])
  #   if message.channel.id == bumpchannel.id:
  #     bumpro = bumpc[0]['bumprole']
  #     await bumpchannel.send(f'It\'s Bump time bois and gorls {bumpro}')
  await bot.process_commands(message)

@bot.command()
async def q(ctx):
  replies_of_q = ['It is certain','Without a doubt','You may rely on it','Yes definitely','It is decidedly so','As I see it, yes','Most likely','Yes','Outlook good','Signs point to y','Reply hazy try again','Better not tell you now','Ask again later','Cannot predict now','Concentrate and ask again','Don\'t count on it','Outlook not so good','My sources say no','Very doubtful','My reply is no']
  await ctx.reply(replies_of_q[randint(0,19)])

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
  x = c_id.update_one({'_id': ctx.channel.name},{"$set": {"box":ctx.channel.id}}, upsert=True)
  await ctx.send(f"Done. <#{ctx.channel.id}> channel is set for receiving complaints")

@bot.command()
async def setbump(ctx):
  bumprole = ctx.message.content[9:]
  roleid.update_one({'_id': 'bumprole'},{"$set": {"bumprole":bumprole}}, upsert=True)
  x = c_id.update_one({'_id': 'bumpremc'},{"$set": {"bumpreminder":ctx.channel.id}}, upsert=True)
  await ctx.send(f"Done. <#{ctx.channel.id}> channel is set for bump remainder")

@bot.command()
async def help(ctx):
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
    await ctx.send(f'Hey <@{el}>, your gorl <@{ella}> asking for hugs you slug')
  else:
    await ctx.send('Sorry fella, only filth can use this command')

@bot.command()
async def htd(ctx):
  n = ctx.message.content[5:]
  x = int(len(n)-1) #3
  def hex_to_deci(x,n):
    hexdictsmall = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15}
    dec = 0
    for i in n:#'1100'
        i = i.lower()
        i = hexdictsmall.get(i)
        if x > -1:
                dec += int(i) * 16**x
                x -= 1
    return dec
  await ctx.send(hex_to_deci(x,n))
@bot.command()
async def setverify(ctx):
  #if vyoxchannel is None:
  msg = await ctx.send('React to verify')
  print(msg.id)
  await msg.add_reaction('✅')
  c_id.update_one({'_id': "verify"},{"$set": {"ver":ctx.channel.id,"vermsgid":msg.id}}, upsert=True)
  ctx.delete()

@bot.command()
async def kata(ctx,diff,lan):
  return 0

@bot.event
async def on_raw_reaction_add(ctx):
  vychannel = c_id.find({})
  msgid = vychannel[3]['vermsgid']
  vyoxchannel = bot.get_channel(vychannel[3]['ver'])
  if msgid == ctx.message_id:
    member = ctx.member
    guild = member.guild
    emoji = ctx.emoji.name
    if emoji == '✅':
      role = discord.utils.get(guild.roles, name="Makkal")
    await member.add_roles(role)
    await ctx.remove_reaction('✅',ctx.message.author)
  
    await bot.process_commands(ctx)

  
bot.run(evvi)