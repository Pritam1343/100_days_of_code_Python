import random
letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
    '[', ']', '{', '}', '<', '>', '/', '|', '~'
]
print("Welcome to the Pypassword generator\n")
print('''
 ____                                     _  
 |  _ \ __ _ ___ _____      _____  _ __ __| | 
 | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | 
 |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | 
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_| 
                                              
''')
ps_letters=int(input("How many letters would you like in password ?\n"))
ps_numbers=int(input("How many numbers would you like  in password ?\n"))
ps_symbols=int(input("How many symbols would you like in password ?\n"))
#password=""
#Simple solution
# pas=""
# for char in range(0,ps_letters):
#     password+=random.choice(letters)
# for num in range(0,ps_numbers):
#     password+=random.choice((numbers))
# for symb in range(0,ps_symbols):
#     password+=random.choice(symbols)
# for char in range(0,len(list(password))):
#     pas+=random.choice(list(password))
# print(pas)
# print("Success!\n"
# "Your password has been successfully created !!!")

#Hard solution
password_list=[]

for char in range(0,ps_letters):
    password_list.append(random.choice(letters))
for num in range(0,ps_numbers):
    password_list.append(random.choice((numbers)))
for symb in range(0,ps_symbols):
    password_list.append(random.choice(symbols))
print(password_list)
random.shuffle(password_list)
password=""
for char in password_list:
    password+=char
print(f"Your password is :{password}")

