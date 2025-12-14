import random

# Raw chrarcters for password generation
symbols = ["!", "@", "#", "$", "%", "(", ")"]
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
           ]
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Data collection
print("Welcome to the PyPassword Generator!") 
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_nums = int(input("How many symbols would you like?\n"))

# Password Creatione

password = ""

for char in range(num_letters):
    random_letter = random.choice(letters)
    password += random_letter

for char in range(num_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

for char in range(num_nums):
    random_num = random.choice(nums)
    password += random_num
    
# Shuffle it up

password = list(password)
random.shuffle(password)
new_password = ''.join(password)

print(f"Your new password is: {new_password}")