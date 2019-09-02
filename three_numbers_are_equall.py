print("Check if 3 numbers are equals")

one = int(input())

two = int(input())

three = int(input())

if one != two:
    print("They are not equals")
elif one != three:
    print("They are not equals")
elif two != three:
    print("They are not equals")
else:
    total = one + two + three
    if total in range(9, 100):
        print("OK")
