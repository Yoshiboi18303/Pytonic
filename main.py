import os
# from duck import command
from event_handler import ready_bot
loginToken = os.environ['TOKEN']

ready_bot(loginToken)

