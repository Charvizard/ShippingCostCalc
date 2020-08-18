premium_shipping = 125

def get_ground_shipping(weight): 
  if (weight <=2) and (weight >= 0):
    cost = weight*1.5
  elif (weight > 2) and (weight <= 6):
    cost = weight*3
  elif (weight > 6) and (weight <= 10):
    cost = weight*4
  elif (weight > 10) :
    cost = weight*4.7
  return cost + 20

def get_drone_shipping(weight) : 
    if (weight <= 2) and (weight >= 0) : 
        cost = weight*4.5
    elif (weight > 2) and (weight <= 6) : 
        cost = weight*9
    elif (weight > 6) and (weight <= 10) : 
        cost = weight*12
    elif (weight > 10) :
        cost = weight*14.25
    return cost

print("How would you like to ship? (Drone or Ground)")
print("You can also choose to see the cheapest option. (Cheapest)")
shipping_method = input()

if (shipping_method == "Drone") : 
    print("How much does your package weigh? (In pounds)")
    weight = float(input())
    cost = get_drone_shipping(weight)
    print(cost)
elif (shipping_method == "Ground") : 
    print("How much does your package weigh? (In pounds)")
    weight = float(input())
    cost = get_ground_shipping(weight)
    print(cost)
elif (shipping_method == "Cheapest") : 
    print("How much does your package weigh? (In Pounds)")
    weight = float(input())
    ground_cost = get_ground_shipping(weight)
    drone_cost = get_drone_shipping(weight)
    if (ground_cost < drone_cost) and (ground_cost < premium_shipping): 
        print("Shipping by ground is a cheaper option and will cost : $" + str(ground_cost))
    elif (drone_cost < ground_cost) and (drone_cast < premium_shipping): 
        print("Shipping by drone is a cheaper option and will cost : $" + str(drone_cost))
    elif (premium_shipping < ground_cost) and (premium_shipping < drone_cost) : 
        print("Shipping by Premium Ground is a cheaper option and will cost : $" + str(premium_shipping))
    else : 
        print("Shipping will cost the same with either method, at : $" + str(ground_cost))

