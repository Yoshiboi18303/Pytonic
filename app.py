# Importing Items
import discord
import os
# from duck import command
from event_handler import ready_bot

# Variables
loginToken = os.environ['TOKEN']

# Function Runners
ready_bot(loginToken)
