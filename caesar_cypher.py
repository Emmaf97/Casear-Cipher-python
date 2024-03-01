letters = "abcdefghijklmnopqrstuvwxyz"

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
                if new_index >= 26:
                    new_index -= 26
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
                    new_index += 26
                plaintext += letters[new_index]
    return plaintext
    
print("Do you want to Encrypt the data or Decrypt the data? ")
user_input = input("e/d: ").lower()


if user_input == "e":
    print("Encryption mode selected")
    print()
    print("Enter the key (1 through 26: )")
    text = input("Enter the text to encrypt")
    
    
elif user_input == "d":
    print("Deccryption mode selected")
    print()
    print("Enter the key (1 through 26: )")
    text = input("Enter the text to decrypt")

