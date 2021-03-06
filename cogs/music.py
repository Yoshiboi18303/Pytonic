import discord
from discord.ext import commands
import youtube_dl

class Music(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command(help="Makes the client join the Voice Channel you're in!", usage="py join", aliases=['connect'])
  async def join(self, ctx):
    if ctx.author.voice is None:
      return await ctx.send("Please join a Voice Channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)
    await ctx.send('Joined the Voice Channel!')
  
  @commands.command(help="Makes the client disconnect from the Voice Channel it's in.", usage="py disconnect", aliases=['dc'])
  async def disconnect(self, ctx):
    await ctx.voice_client.disconnect()
    await ctx.send('Disconnected from the Voice Channel.')

  @commands.command(help="Starts playing music in the Voice Channel you're in!", usage="py play <song_link>")
  async def play(self, ctx, url):
    if ctx.author.voice is None:
      return await ctx.send("Please join a Voice Channel!")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format':"bestaudio"}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(help="Pauses the music that is playing in the Voice Channel you're in!", usage="py pause")
  async def pause(self, ctx):
    await ctx.voice_client.pause()
    await ctx.send('Paused the music!')

def setup(client):
  client.add_cog(Music(client))