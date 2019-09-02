print("Print digit without loop")
i = input(input("Enter a digit"))


def count_digit(number, count=0):
    if number > 0:
        number = number // 10
        count += 1
        return count_digit(number, count)
    else:
        return count


print(count_digit(i))
