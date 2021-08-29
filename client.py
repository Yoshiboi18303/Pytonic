import discord
from discord.ext import commands
from help import CustomHelpCommand

client = commands.Bot(command_prefix="py ", help_command=CustomHelpCommand())