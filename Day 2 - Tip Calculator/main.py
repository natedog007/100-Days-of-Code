print("Welcome to the Tip Calculator!")
bill_total = float(input("What was the total bill? "))
tip_amount = float(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split bill? "))

bill_plus_tip = bill_total + (bill_total * ((tip_amount) * .01))
bill_plus_tip_split = (bill_plus_tip / num_people)

print(f"Each person should pay: ${bill_plus_tip_split:.2f}")

