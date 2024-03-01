letters = "abcdefghijklmnopqrstuvwxyz"

#Example 
# key = 3
# a -> d , g -> j 

print("Do you want to Encrypt the data or Decrypt the data? ")
user_input = input("e/d: ").lower()


if user_input == "e":
    print("Encyption mode selected")
    print()
    print("Enter the key (1 through 26: )")
    text = input("Enter the text to encrypt")
    

