print("Basic gross salary")

hra = 0
da = 0
ta = 0
oh = 0

print("Enter your salary ")
salary = int(input())

if salary < 10000:
    hra = salary * 0.3
    da = salary * 0.9
    ta = salary * 0.1
    oh = 4532
else:
    hra = salary * 0.35
    da = salary * 1.10
    ta = salary * 0.12
    oh = 9535

base_salary = salary + (hra + da + ta + oh)
print("HRA :", str(hra))
print("DA :", str(da))
print("TA :", str(ta))
print("OH :", str(oh))

print(base_salary)
