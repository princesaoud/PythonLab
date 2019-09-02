print("Five the subjects marks")

subj = {"python": int(input("Enter Python mark ")), "java": int(input("Enter Java mark ")), "c#": int(input("Enter c# mark ")),
        "Database": int(input("Enter Database mark ")), "Statistics": int(input("Enter Statistics mark "))}
total = 0
percentage = 0
for i,v in subj.items():
    total += v
    print(i,v)

percentage = total * 0.2
print("Total ", str(total))
print("Percentage of student :", str(percentage)+" %")
