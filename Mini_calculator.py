print("Mini calculator")

choice = "y"

while choice == "yes" or choice == "y":

    print("enter one number ")
    one = int(input())

    print("enter one number ")
    two = int(input())

    print("press 1 to add")
    print("press 2 to substract")
    print("press 3 to multiply")
    print("press 4 to divide")
    choice = input()

    if choice == 1:
        print("{0} + {1} = {2} ".format(one, two, one + two))
    elif choice == 2:
        print("{0} - {1} = {2} ".format(one, two, one - two))
    elif choice == 3:
        print("{0} * {1} = {2} ".format(one, two, one * two))
    elif choice == 4:
        print("{0} / {1} = {2} ".format(one, two, one / two))

    print ("Do you want to do more ?")
    choice = raw_input()
