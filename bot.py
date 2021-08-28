import discord
import os
# from duck import command
from event_handler import ready_bot
from website import website
loginToken = os.environ['TOKEN']

website("Pytonic", "An upcoming bot from Yoshiboi18303!", "0.0.0.0", 5000)
ready_bot(loginToken)