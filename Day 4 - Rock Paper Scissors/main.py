import random

user_input = int(input("What do you Choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors \n"))
computer_choice = random.randint(0, 2)

print(f"You chose {user_input}")
print(f"The computer chose {computer_choice}")

# Comparison
if computer_choice == user_input:
    print("It's a tie")
elif user_input == 0 and computer_choice == 2:
    print("You Win!")
elif computer_choice == 0 and user_input == 2:
    print("You lose")
elif computer_choice > user_input:
    print("You Lose")
else:
    print("You typed the wrong number.")
    




    
