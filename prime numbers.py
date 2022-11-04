lst_number = [i for i in map(int, input("Enter your number:").strip())]
check_digit = lst_number.pop()
lst_number.reverse()

lst_check = []

for index, value in enumerate(lst_number):
    if index % 2 == 0 :
        value *= 2
        if value > 9:
            value -= 9
        lst_check.append(value)
    else:
        lst_check.append(value)


total = sum(lst_check) + int(check_digit)

if total % 10 == 0:
    print("Valid number")
else:
    print("Invalid number")
