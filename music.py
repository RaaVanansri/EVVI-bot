from ast import alias
import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True, alias=['j',['J']])
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send('You\'re not in a voice channel')
        vc = ctx.author.voice.channel
        if ctx.voice_client is None:
            await vc.connect()
        else:
            await ctx.voice_client.move_to(vc)

    @commands.command(pass_context = True, alias=['dc'])
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command(pass_context = True, alias=['p'])
    async def play(self,ctx,url):
        #ctx.voice_client.stop()
        FFMPEG_OPTIONS = {
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'}
        YDL_O = {'format':'bestaudio'}
        #vc1 = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_O) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            vc = ctx.author.voice.channel
            if ctx.author.voice is None:
                await ctx.send('You\'re not in a voice channel')
            if ctx.voice_client is None:
                await vc.connect()
                ctx.voice_client.play(await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS))
            

    @commands.command(pass_context = True, alias=['pa'])
    async def pause(self, ctx):
        await ctx.voice_client.pause()

    @commands.command(pass_context = True, alias=['res'])
    async def resume(self, ctx):
        await ctx.voice_client.resume()

def setup(client):
    client.add_cog(music(client))