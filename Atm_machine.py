print("Atm machine 100,500,2000")

print("how much do you want to withdraw")
amount = input()
receipt = {"2000": 0, "500": 0, "100": 0}
note = 10000
if amount >= 2000:
    while note*2000 > amount:
        print("How many 2000 notes do you want ?","remaining balance is ",str(amount))
        note = input()
    receipt["2000"] += note
    amount -= (2000*note)

note = 10000
if amount >= 500:
    while note * 500 > amount:
        print("How many 500 notes do you want ?","remaining balance is ",str(amount))
        note = input()
    receipt["500"] += note
    amount -= (500*note)

note = 10000
if amount >= 100:
    while note * 100 > amount:
        print("How many 100 notes do you want ?","remaining balance is ",str(amount))
        note = input()
    receipt["100"] += note
    amount -= (100*note)

if amount < 100:
    print("you have withdraw all possible amount")
    print("Check your receipt")
    print(receipt)