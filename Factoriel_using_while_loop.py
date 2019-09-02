print("Factorial using while loop")
number = int(input("Enter a number"))
temp = number
while temp > 1:
    temp -= 1
    number = number * temp

print(number)
