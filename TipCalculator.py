print("Welcome to the tip calculator!")
bill = input("What was the total bill?\n")
tip = input("How much tip woud you like to give?\n")
split = input("How many people to split the bill?\n")

bill1 = float(bill)
tip1 = int(tip)
split1 = int(split)

tip2 = tip1/100
totalTip = bill1 * tip2
# print(totalTip)
totalAmout = bill1 + totalTip
# print(totalAmout)
totalPeople = totalAmout / split1
finalAmount = round(totalPeople, 2)
print(f"Each person should pay: ${finalAmount}" )
