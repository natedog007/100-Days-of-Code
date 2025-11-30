print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice_1 = str(input("Go left or right? "))

if choice_1 == "left":
    print("A lake appears...")
else:
    print("Fell into a hole \n GAME OVER")
    quit()
    
choice_2 = str(input("Go swim or wait? "))

if choice_2 == "wait":
    print("A three doors appear... One is Red, one is Blue, and the other is Yellow...")
else:
    print("Eaten by Trout \n GAME OVER")
    quit()

choice_3 = str(input("Go in red, blue, or yellow? "))

if choice_3 == "red":
    print("Burned by Fire \n GAME OVER")
    quit()
elif choice_3 == "blue":
    print("Eaten by Beasts \n GAME OVER")
    quit()
elif choice_3 == "yellow":
    print("You Win!")
else:
    print("Game Over")
    quit()
    
    