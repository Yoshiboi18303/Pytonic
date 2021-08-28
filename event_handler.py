import discord

def ready_bot(client_token):
  from client import client
  @client.event
  async def on_ready():
    print("The client is ready.")
  @client.command()
  async def ping(ctx):
    print("Running command \"ping\"")
    await ctx.send("Pong!")
  client.run(client_token)
