print("Fibonacci series")

x = 0
dev = 1
apr = 1
fibo = 0

print("1 1"),
while x < 10:
    fibo = dev + apr
    print(str(fibo)),
    temp = dev
    dev = fibo
    apr = temp
    x += 1
