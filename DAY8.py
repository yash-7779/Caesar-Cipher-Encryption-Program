# Caeser Cipher encryption code : 

logo = '''           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
'''
print(logo)



alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# direction = input("Type 'encode' to encrypt or 'decode' to decrypt the message:\n").lower()


# def encrypt(text, shift_amount):
#     encrypted_text = ""
#     for letter in text:
#         index = alphabets.index(letter)
#         new_index = index + shift_amount
#         if new_index >= 26:
#             new_index -= 26
#         encrypted_text += alphabets[new_index]
#     print(f"The encoded message is '{encrypted_text}'.")



# def decrypt(text, shift_amount):
#     decrypted_text = ""
#     for letter in text:
#         index = alphabets.index(letter)
#         new_index = index - shift_amount
#         decrypted_text += alphabets[new_index]
#     print(f"The decrypted text is '{decrypted_text}'.")


# if direction == "encode":
#     message = input("Type your message:\n").lower()
#     shift = int(input("Enter shift number:\n"))
#     encrypt(message, shift)
# elif direction == "decode":
#     message2 = input("Enter the message:\n").lower()
#     shift2 = int(input("Enter the shift amount:\n"))
#     decrypt(message2, shift2)
# else:
#     print("Invalid input!")



# def cipher(text, shift_amount, direction):
#     plain_text = ""

#     if direction == "encode":
#         for letter in text:
#             if letter in alphabets:
#                 index = alphabets.index(letter)
#                 new_index = index + shift_amount
#                 if new_index >= 26:
#                     while new_index >= 26:
#                         new_index -= 26
#                 plain_text += alphabets[new_index]
#             else:
#                 plain_text += letter
#     elif direction == "decode":
#         for letter in text:
#             if letter in alphabets:
#                 index = alphabets.index(letter)
#                 new_index = index - shift_amount
#                 plain_text += alphabets[new_index]
#             else:
#                 plain_text += letter
#     else:
#         print("Invalid Input!! ")
#     print(f"The {direction}d message is '{plain_text}'.")


# text3 = input("Enter your message: ").lower()
# shift3 = int(input("Enter shift amount: "))
# direction = input("Type 'encode' to encrypt or 'decode' to derypt the message: ").lower()

# cipher(text3, shift3, direction)


def cipher(text, shift_amount, direction):
    plain_text = ""

    if direction == "encode":
        for letter in text:
            if letter in alphabets:
                index = alphabets.index(letter)
                new_index = index + shift_amount
                if new_index >= 26:
                    while new_index >= 26:
                        new_index -= 26
                plain_text += alphabets[new_index]
            else:
                plain_text += letter
    elif direction == "decode":
        for letter in text:
            if letter in alphabets:
                index = alphabets.index(letter)
                new_index = index - shift_amount
                plain_text += alphabets[new_index]
            else:
                plain_text += letter
    else:
        print("Invalid Input!! ")
    print(f"The {direction}d message is '{plain_text}'.")

repeat = True

while repeat:
    text3 = input("Enter your message: ").lower()
    shift3 = int(input("Enter shift amount: "))
    direction = input("Type 'encode' to encrypt or 'decode' to derypt the message: ").lower()

    cipher(text3, shift3, direction)

    restart = input("Type 'yes' if you want to go again. otherwise type 'no' : ")

    if restart == "yes":
        repeat = True
    else:
        repeat = False
        print("GOODBYE!!")
 




