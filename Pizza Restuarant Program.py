# Standard pizza sizes
SMALL = 3.25
MEDIUM = 5.50
LARGE = 7.15
# Extra toppings
EXTRA_TOPPING1 = 0.75
EXTRA_TOPPING2 = 1.35
EXTRA_TOPPING3 = 2
EXTRA_TOPPING4 = 2.50

DISCOUNT = 0.1

DELIVERY_CHARGE = 2.50

MINIMUM_pizzaNum = 1
MAXIMUM_pizzaNum = 6

def validate_pizzaNum(pizzaNum):
    while pizzaNum < MINIMUM_pizzaNum or pizzaNum > MAXIMUM_pizzaNum:
        print("Invalid Input")
        pizzaNum = int(input("How many pizzas would you like to order?: "))
    return pizzaNum


staff_name = str(input("Enter your name: "))
address = input("Enter your address: ")
phoneNum = int(input("Enter your phone number: "))

pizzaNum = int(input("How many pizzas would you like to order?: "))
pizzaNum = validate_pizzaNum(pizzaNum)

total_cost = 0

for i in range(0,pizzaNum):
    # pizza size charge
    pizza_size = input(f"Enter the size of pizza number {i+1} (small, medium, large): ").lower()
    if pizza_size == "small":
        cost_size = SMALL
    elif pizza_size == "medium":
        cost_size = MEDIUM
    elif pizza_size == "large":
        cost_size = LARGE
    else:
        print("Invalid input. Defaulting to medium.")
        cost_size = MEDIUM
    total_cost += cost_size
    # toppings charge
    toppingsNum = int(input("How many toppings do you want?: "))
    if toppingsNum == 1:
        cost_toppings = EXTRA_TOPPING1
    elif toppingsNum == 2:
        cost_toppings = EXTRA_TOPPING2
    elif toppingsNum == 3:
        cost_toppings = EXTRA_TOPPING3
    elif toppingsNum >= 4:
        cost_toppings = EXTRA_TOPPING4
    else:
        cost_toppings = 0
    total_cost += cost_toppings

if total_cost > 20:
    total_cost2 = total_cost*DISCOUNT
    print("Congrats! You're eligible for the 10% discount")
else:
    pass
# delivery charge
deliveryRequest = input("Do you want your order to be delivered using our delivery service? (yes or no): ").lower()
if deliveryRequest == "yes":
    delivery_cost = 2.50
    total_cost2 += delivery_cost
elif deliveryRequest == "no":
    delivery_cost = 0
else:
    print("Invalid input. Defaulting to no")
    
print("----BILL----") 
print(f"Costumer's Name: {staff_name}") 
print(f"Address:{address}")
print(f"Phone Number: {phoneNum}")
print(f"subtotal cost: {total_cost} ")
print(f"discount: {total_cost*DISCOUNT}") 
print(f"Delivery charge: {delivery_cost}")
print(f"Total charge: {total_cost2}")



    
        
    