import discord
from discord.ext import commands
import os
import json
# from website import start_website

def ready_bot(client_token):
  from client import client

  # start_website("Pytonic", "An upcoming bot from Yoshiboi18303!", "0.0.0.0", 5000)
  @client.event
  async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Python'))
    print("The client is ready.")
    for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
  @client.event
  async def on_member_join(member):
    print(f'{member} has joined a server that the client is in!')
  @client.event
  async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('Please pass in all required arguments.')
    elif isinstance(error, commands.MissingPermissions):
      await ctx.send('You don\'t have the correct permissions to run this command!')

  @client.event
  async def on_guild_join(guild):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
      guild.id = str(guild.id)
    prefixes[guild.id] = "py "

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=2)
  
  @client.event
  async def on_guild_remove(guild):
    with open('prefixes.json', 'r') as f:
      prefixes = json.load(f)
    guild.id = str(guild.id)
    prefixes.pop(guild.id)   

    with open('prefixes.json', 'w') as f:
      json.dump(prefixes, f, indent=2)

  @client.event
  async def on_message(msg):
    try: 
      if msg.mentions[0] == client.user:
        with open('prefixes.json', 'r') as f:
          prefixes = json.load(f)
        pre = prefixes[msg.guild.id]
        await msg.channel.send(f'My prefix in {msg.guild.name} is {pre}.')
    except:
      pass

  @client.command(help="Loads a cog.")
  @commands.has_permissions(manage_guild=True)
  async def load(ctx, extension):
    print("Running command \"load\"")
    await ctx.send(f"Loaded cog \"cogs.{extension}\"")
    client.load_extension(f'cogs.{extension}')

  @client.command(help="Unloads a cog.")
  @commands.has_permissions(manage_guild=True)
  async def unload(ctx, extension):
    print("Running command \"unload\"")
    await ctx.send(f"Unloaded cog \"cogs.{extension}\"")
    client.unload_extension(f'cogs.{extension}')

  @client.command(help="Reloads a cog.")
  @commands.has_permissions(manage_guild=True)
  async def reload(ctx, extension):
    print("Running command \"reload\"")
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f"Reloaded cog \"cogs.{extension}\"")
  client.run(client_token)