import discord
from discord.ext import commands

class Moderation(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command(help="Clears a end-user specified amount of messages!")
  async def clear(self, ctx, amount=5):
    amount = amount + 1
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages from this channel!')

  
  
def setup(client):
  client.add_cog(Moderation(client))