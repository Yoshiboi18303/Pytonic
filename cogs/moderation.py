import discord
from discord.ext import commands

class Moderation(commands.Cog):
  
  def __init__(self, client):
    self.client = client

  @commands.command(help="Clears a end-user specified (or default 5) amount of messages!", aliases=['purge'])
  async def clear(self, ctx, amount=5):
    amount = amount + 1
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Cleared {amount} messages from this channel!')
  
  @commands.command(help="Kicks a member from the current server!", aliases=['boot'])
  async def kick(self, ctx, *, member : discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send('👢 Kicked the member, buh-bye! 👢')
  
  @commands.command(help="Bans a member from the current server!", aliases=['hammer'])
  async def ban(self, ctx, *, member : discord.Member, reason=None):
    await member.ban(reason=reason)
    await ctx.send('🔨 Banned the member, get hammered! 🔨')

  @commands.command(help="Unbans a member from the current server!", aliases=['forgive'])
  async def unban(self, ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    # if member_name or member_discriminator == None:
    #  return await ctx.send('There\'s not enough values to unpack, please provide the username and the discriminator of the user you want to unban!')

    for ban_entry in banned_users:
      user = ban_entry.user

      if (user.name, user.discriminator) == (member_name, member_discriminator):
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user.name}#{user.discriminator}!')
  
def setup(client):
  client.add_cog(Moderation(client))