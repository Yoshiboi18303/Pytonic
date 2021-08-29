import discord
from discord.ext import commands
from utils.prefix_methods import get_prefix

client = commands.Bot(command_prefix=get_prefix, intents = discord.Intents.all())