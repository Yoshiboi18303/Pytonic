import json
from utils.errors import refer_err

def get_prefix(client, message):
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  return prefixes[str(message.guild.id)]

def change_prefix(guild, prefix):
  if guild is None:
    refer_err(guild)
  if prefix is None:
    refer_err(prefix)
  
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)] = str(prefix)

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=2)

def remove_prefix(guild):
  if guild is None:
    refer_err(guild)
  
  with open('prefixes.json', 'r') as f:
    prefixes = json.load(f)

  prefixes[str(guild.id)]

  with open('prefixes.json', 'w') as f:
    json.dump(prefixes, f, indent=4)