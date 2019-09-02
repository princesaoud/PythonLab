print("Print Amstrong number")

number = str(input("Enter a number "))
myList = []
for i in number:
    myList.append(i)

temp = 0
for i in myList:
    temp += pow(int(i), 3)

if temp == int(number):
    print("The entered number is an Amstrong number ")
else:
    print("The entered number is not an Amstrong number ")
