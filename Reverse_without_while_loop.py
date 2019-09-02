print("Reverse without using while loop")
digit = str(input("Enter a number"))
li = []
for x in digit:
    li.append(x)

li.reverse()
number = int("".join(li))
print(number)

