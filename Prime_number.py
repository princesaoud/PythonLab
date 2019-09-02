print("Prime number ")
y = "yes"


def prime_number():
    number = input("Enter a number i said a number enter a bullshit and ill kill you ")

    temp = 1
    prime = True
    while temp < number / 2:
        temp += 1
        print(number, temp, number/temp)
        if number % temp == 0:
            prime = False
            break

    if not prime:
        print("Not prime")
    else:
        print("It is prime")


while y == "yes" or y == "y":
    prime_number()
    y = input("Do you want to test more ?")
