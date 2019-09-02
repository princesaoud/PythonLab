print("Reverse number using loop")
digit = str(input("Enter a number"))
li = []
i = 0
while i < len(digit):
    li.append(digit[i])
    i += 1

li.reverse()
number = int("".join(li))
print(number)
