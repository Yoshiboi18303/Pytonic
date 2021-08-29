import discord
from discord.ext import commands
from utils.prefix_methods import change_prefix

class Prefix(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command(help="Changes the default prefix for the current server!", aliases=['prefix','cp','chp','changep'], usage="py changep <new prefix>")
  @commands.has_permissions(manage_guild=True)
  async def changeprefix(self, ctx, prefix):
    if prefix is None:
      return await ctx.send('You need to define a prefix to change to!')
    prefix = str(prefix)
    await ctx.send(f'You have successfully changed the prefix to {prefix}!')
    # embed = discord.Embed(title="Prefix Changed!", color=discord.Color.green(), description=f"You have successfully changed the prefix for {ctx.guild.name} to {prefix}!")
    await change_prefix(ctx.guild, prefix)
  
def setup(client):
  client.add_cog(Prefix(client))