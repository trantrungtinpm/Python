import math


def simple_equation (a, b):
    if a == 0 :
        if b == 0 :
            return "Phương trình có vô số nghiệm"
        return "Phương trình vô nghiệm"
    else:

        return "x={}".format(-b / a)


def quadratic_equation(a, b, c):
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        return "x1 = x2 = {}".format(-b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return "x1= {}\nx2= {}".format(x1, x2)


mode = int(input("Chọn chế độ:"))


if mode != 1 and mode != 2:
    print("Vui lòng chọn một trong hai chức năng")
    print("1.Gia3i phương trình bậc nhất\n2.Giaỉ phương trình bậc hai")
elif mode == 1:
    a, b = map(float,input().split())
    print(simple_equation(a, b))
else:
    a, b, c = map(float,input().split())
    print(quadratic_equation(a, b, c))



