import discord
from discord.ext import commands
import os
loginToken = os.environ['TOKEN']

class Ready(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  
def setup(client):
  client.add_cog(Ready(client))
