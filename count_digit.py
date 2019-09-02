print("Count digit with loop")
i = int(input("Enter a digit"))
n = 0
while i > 0:
    i = i // 10
    n += 1

print(n)
