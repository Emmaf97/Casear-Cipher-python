letters = "abcdefghijklmnopqrstuvwxyz"
num_letters = len(letters)
#Example 
# key = 3
# a -> d , g -> j 

def encrypt(plaintext, key):
    ciphertext = ""
    for letter in plaintext:                            # Going through the entered text and checking that the letter is in our letters variable.
                                                        # If the letter entered is a special character not in the variable we add that as is.
                                                        # Then we get the index of the index of letters and add the key to it to shift the letters.
                                                        
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                ciphertext + letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext
        
        
def decrypt(ciphertext, key):
    plaintext = ""
    for letter in ciphertext:                           
                                                        
        letter = letter.lower()
        if not letter == " ":
            index = letters.find(letter)
            if index == -1:
                plaintext + letter
            else:
                new_index = index - key
                if new_index < 0:
                    new_index += num_letters
                plaintext += letters[new_index]
    return plaintext
    
print("Do you want to Encrypt the data or Decrypt the data? ")
user_input = input("e/d: ").lower()


if user_input == "e":
    print()
    print("Encryption mode selected")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to encrypt: ")
    ciphertext = encrypt(text, key)
    print(f"CIPHERTEXT: {ciphertext}")
    
    
elif user_input == "d":
    print()
    print("Deccryption mode selected")
    print()
    key = int(input("Enter the key (1 through 26): "))
    text = input("Enter the text to decrypt: ")
    plaintext = decrypt(text,key)
    print(f"PLAINTEXT: {plaintext}")

