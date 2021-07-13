from string import ascii_letters

def encrypt(string, key = 3):
    alpha = ascii_letters
    result = ""
    for ch in string:
        if ch not in alpha:
            result += letter
        else:
            new_key = (alpha.index(ch)+ key) % len(alpha)
            result += alpha[new_key]
    print(result)

def decrypt(string, key = 3):
    alpha = ascii_letters
    decrypt_result = ""
    for ch in string:
        if ch not in alpha:
            decrypt_result += ch
        else:
            new_key = (alpha.index(ch)- key) % len(alpha)
            decrypt_result += alpha[new_key]
    print(decrypt_result)



encrypting_type = input("what is your cypher type ? Ceaser or PigPen \n")
if encrypting_type == "ceaser" or encrypting_type == "pigpen":
    user_action = input("what do you want to do with your text? Encrypt or Decrypt \n")
    if user_action == "encrypt" or user_action == "decrypt":
        user_text = input("please type your text \n")
    else: 
        print("Error")
else: 
    print("Error")


if encrypting_type.lower() == "ceaser" and user_action.lower() == "encrypt":
    encrypt(user_text)
if encrypting_type.lower() == "ceaser" and user_action.lower() == "decrypt":
    decrypt(user_text)
