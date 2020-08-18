def get_ground_shipping(weight): 
  if (weight <=2):
    cost = weight*1.5
  elif (weight > 2) and (weight <= 6):
    cost = weight*3
  elif (weight > 6) and (weight <= 10):
    cost = weight*4
  elif (weight > 10) :
    cost = weight*4.7
  return cost + 20

print("How much does your package weigh? (In pounds)")
weight = float(input())
cost = get_ground_shipping(weight)
print(cost)

