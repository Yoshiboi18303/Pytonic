import discord

def duck_info(duck_name, year_of_extinction):
  return f'Your duck {duck_name} will be extinct in the year {year_of_extinction}'
def extinction_check(duck_name, is_extinct):
  is_extinct = bool(is_extinct)

  if is_extinct:
    return f'Your duck {duck_name} is extinct.'
  else:
    return f'Your duck {duck_name} is not extinct.'