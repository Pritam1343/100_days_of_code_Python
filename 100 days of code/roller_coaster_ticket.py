print("Welcome to Python Pizza Deliveries")
size = input("What is the size of pizza do you want? S, M or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N:\n")
extra_cheese = input("Do you want extraa cheese? Y or N:\n")
Bill = 0
if size == "S":
    Bill = 15
    if pepperoni == "Y":
        Bill += 2
    if extra_cheese == "Y":
        Bill += 1
elif size == "M" :
    Bill = 20
    if pepperoni == "Y":
        Bill += 3
    if extra_cheese == "Y":
        Bill += 1
elif size == "L":
    Bill = 25
    if pepperoni == "Y":
        Bill += 3
    if extra_cheese == "Y":
        Bill += 1
else:
    print("You have entered wrong input !!")
print(f"Your final bill is ${Bill}")
