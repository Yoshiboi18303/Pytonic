import discord
import random
import json
from discord.ext import commands
from utils.account_methods import open_account, get_bank_data, update_bank

class Economy(commands.Cog):

  def __init__(self, client):
    self.client = client
  
  @commands.command(help="Shows the balance of you!", aliases=['bal'], usage="py balance")
  async def balance(self, ctx):
    return await ctx.send("This command needs to be fixed, please wait for a bit!")
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

    earnings = random.randrange(2, 101)

    await ctx.send(f'You begged someone and have earned {earnings} coins after begging!')

    users[str(ctx.author.id)]['wallet'] += earnings
    
    with open('mainbank.json', 'w') as f:
      json.dump(users, f)

  @commands.command(help="Withdraw some money from your bank!", aliases=['wd'], usage="py withdraw <money>")
  async def withdraw(self, ctx, amount=None):
    # return await ctx.send('Coming soon!')
    await open_account(ctx.author)

    if amount is None:
      return await ctx.send('Please specify an amount to withdraw!')
    bal = await get_bank_data(ctx.author)
    amount = int(amount)
    
    if amount > bal[1]:
      return await ctx.send("You don't have that much money in your bank!")
      return
    if amount < 0:
      return await ctx.send("That's a negative change, the change needs to be positive integer (number)!")

    await update_bank(ctx.author, amount)
    await update_bank(ctx.author, -1*amount, "bank")

    await ctx.send(f"You have successfully withdrawn {amount} coins from your bank!")

def setup(client):
  client.add_cog(Economy(client))