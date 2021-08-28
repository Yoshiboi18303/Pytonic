import discord
from discord.ext import commands

class Other(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command(help="Returns \"Pong\" to the end-user!")
  async def ping(self, ctx):
    await ctx.send('Pong!')
  
  @commands.command(help="Returns the name of the client.")
  async def cname(self, ctx):
    await ctx.send('The client name is Pytonic!')
  
  @commands.command(help="Returns the owner of the client.")
  async def owner(self, ctx):
    await ctx.send('The owner of this bot is Yoshiboi18303!')
  
def setup(client):
  client.add_cog(Other(client))