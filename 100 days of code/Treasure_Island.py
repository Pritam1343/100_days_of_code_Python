print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to treasure island !!")
print("Your mission is to find the treasure")
step1 = input('You\'re at a cross road. Where do you want go?\n'
            'Type "left" or "right"\n').lower()
if step1 == "left":
    step2 = input('You\'ve come to lake. There is an island in the middle of the lake.\n'
                 'Type "wait" to wait for a boat. Type "swim" to swim across\n').lower()
    if step2 =="wait":
        step3=input("You arrive at the island unharmed. There is a house with 3 doors"
                    "One red , one yellow and one blue.  Which colour do you choose?\n").lower()
        if((step3=="red")or(step3=="blue")):
            print("Game over !!")
        elif(step3=="yellow"):
            print("You win!")
    elif(step2=="swim"):
        print("Game over !!")
    else:
        print("You have entered wrong input !!")
elif step1 == "right" or step1=="Right":
    print("You fell into a hole. Game over !!")
else:
    print("You have entered wrong input!!")
