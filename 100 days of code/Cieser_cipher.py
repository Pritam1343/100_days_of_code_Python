alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']



def encrypt(orignal_text, shift_amount):
    encrypted_string = ""
    for letter in orignal_text.lower():
        if letter in alphabets:
            ind = alphabets.index(letter)
            mod_ind = ind + shift_amount
            if mod_ind > 25:
                mod_ind = mod_ind % 25 - 1
            encrypted_string += alphabets[mod_ind]
        else:
            encrypted_string += letter
    return encrypted_string


# print(encrypted_text)

def decrypt(encrypted_text, shift_amount):
    decrypted_string = ""
    for letter in encrypted_text:
        if letter in alphabets:
            ind = alphabets.index(letter)
            mod_ind = ind - shift_amount
            decrypted_string += alphabets[mod_ind]
        else:
            decrypted_string += letter
    return decrypted_string


shall_continue = True
while shall_continue:
    orignal_text = input("Enter the string you want to encrypt and decrypt\n")
    shift_amount = int(input("Enter the shift amount\n"))
    encrypted_text = encrypt(orignal_text, shift_amount)
    decrypted_text = decrypt(encrypted_text, shift_amount)

    print(f"Encrypted text is :{encrypted_text}")
    print(f"Decrypted text is :{decrypted_text}")
    cont=input("You want to continue ? Y/N\n")
    if cont.lower()=="y":
        continue
    elif cont.lower()=="n":
        shall_continue=False
        print("Goodbye")
    else:
        print("You have entered wrong input !!")
        shall_continue=False




