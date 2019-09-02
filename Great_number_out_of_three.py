print("Greatest number out of 3")

number = [int(input("Enter a number : ")), int(input("Enter a number : ")), int(input("Enter a number : "))]

number.sort()
print("The greatest number is "+str(number[2]))
print("The smallest number is "+str(number[0]))


