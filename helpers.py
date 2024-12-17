from math import ceil

def retailer_points(name):
  points = 0

  for char in name:
    if char.isalnum():
      points += 1

  return points

def whole_number_total(price):
  if float(price) % 1 == 0:
    return 50
  else:
    return 0

def quarter_multiple(price):
  if float(price) % .25 == 0:
    return 25
  else:
    return 0

def pair_points(num_items):
  return int(f"{num_items / 2}".split('.')[0]) * 5

def odd_date_points(date):
  day = date.split('-')[2]

  if int(day) % 2 != 0:
    return 6
  else:
    return 0

def time_points(time):
  # I'm assuming the format is of the times will be consistent
  if '14:00' < time < '16:00':
    return 10
  else:
    return 0

def description_length(desc,price):
  trimmed = desc.strip()

  if len(trimmed) % 3 == 0:
    return ceil(float(price) * .2)

  return 0

# Main point calculator
def point_calculator(receipt):
  points = 0

  points += retailer_points(receipt['retailer'])
  points += whole_number_total(receipt['total'])
  points += quarter_multiple(receipt['total'])
  points += pair_points(len(receipt['items']))
  for item in receipt['items']:
    points += description_length(item['shortDescription'],item['price'])
  points += odd_date_points(receipt['purchaseDate'])
  points += time_points(receipt['purchaseTime'])

  return points
