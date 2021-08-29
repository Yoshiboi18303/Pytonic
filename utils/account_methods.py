import json
from utils.errors import refer_err, type_err

async def open_account(user):
  if user is None:
    refer_err(user)
    users = await get_bank_data()

    if str(user.id) in users:
      return False
    else:
      users[str(user.id)] = {}
      users[str(user.id)]['wallet'] = 250
      users[str(user.id)]['bank'] = 0

    with open('mainbank.json', 'w') as f:
      json.dump(users, f, indent=2)
    return True

# async def close_account(user):
#   users = await get_bank_data()
#
#   if str(user.id) in users:
#     users.pop()

async def get_bank_data():
  with open('mainbank.json', 'r') as f:
    users = json.load(f)

  return users

async def update_bank(user, change = 0, mode = "wallet"):
  mode = str(mode)
  if user is None:
    refer_err(user)
  if mode != "wallet" or "bank":
    type_err('"wallet" or "bank"')
  users = await get_bank_data()

  users[str(user.id)][str(mode)] += change

  with open('mainbank.json', 'w') as f:
      json.dump(users, f, indent=2)

  bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
  return bal