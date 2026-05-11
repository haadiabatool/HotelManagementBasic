# Resturant Management System

#Define the Menu
menu={
    'Pizza':40,
    'Pasta' :50,
    'Burger' :60,
    'Salad' :70,
    'Coffee': 80 
}

#Greet
print("Welcome to our Resturant. Here's the menu:\n")

# Dict ko ilag line mein print krwany ky liye.
for key, value in menu.items():
    print(f"{key}:Rs.{value}")

# ya variable total price store kry ga.
totalPrice=0

# Conditions
order1=str(input("Enter your first  Order=").capitalize())
if order1 in menu:   
    totalPrice+=menu[order1]
    print(f"Order of {order1} has been added.")
else:
    print(f"{order1} is not present yet!\n Order something else.")
print("Do you want to Order something else?(Yes/No)")
anotherOrder=str(input().capitalize())

if anotherOrder=='Yes':
    order2=str(input(("Enter another Order=")).capitalize())
    if order2 in menu:
        totalPrice+=menu[order2]
        print(f"Order of {order1} and {order2} has been added. ")
    else:
        print(f"{order2} is not present yet!\n Order something else.")
else:
    print("Your Order will be ready soon.")

# Print Total price.
print(f"Total amount of Order= {totalPrice}.")


