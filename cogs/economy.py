import discord
import random
import json
from discord.ext import commands
from utils.account_methods import open_account, get_bank_data

class Economy(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(help="Shows the balance of you!", aliases=['bal'], usage="py balance")
  async def balance(self, ctx):
    await open_account(ctx.author)
    
    users = await get_bank_data()

    wallet_amount = users[str(ctx.author.id)]['wallet']
    bank_amount = users[str(ctx.author.id)]['bank']

    bem = discord.Embed(title=f"{ctx.author.name}'s Balance!", color=discord.Color.green())
    bem.add_field(name="Wallet", value=wallet_amount)
    bem.add_field(name="Bank", value=bank_amount)
    await ctx.send(embed=bem)
  
  @commands.command(help="Beg someone for money!", usage="py beg")
  async def beg(self, ctx):
    await open_account(ctx.author)
    
    users = await get_bank_data()

    earnings = random.randrange(101)

    await ctx.send(f'You begged someone and have earned {earnings} coins after begging!')

    users[str(ctx.author.id)]['wallet'] += earnings
    
    with open('mainbank.json', 'w') as f:
      json.dump(users, f)

def setup(client):
  client.add_cog(Economy(client))