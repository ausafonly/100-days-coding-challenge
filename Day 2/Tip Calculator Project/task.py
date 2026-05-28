print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

split_bill = bill / people
print(f"Split bill: ${split_bill:.2f}")
tip_percent = split_bill * tip / 100
print(f"Tip per person: ${tip_percent:.2f}")
each_person_pay = split_bill + tip_percent
total_bill = round(each_person_pay, 2)
print(f"Each person should pay: ${total_bill}")