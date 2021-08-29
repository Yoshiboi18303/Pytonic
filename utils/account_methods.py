import json

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
      return False
    else:
      users[str(user.id)] = {}
      users[str(user.id)]['wallet'] = 250
      users[str(user.id)]['bank'] = 0

    with open('mainbank.json', 'w') as f:
      json.dump(users, f, indent=4)
    return True

async def get_bank_data():
  with open('mainbank.json', 'r') as f:
    users = json.load(f)

  return users