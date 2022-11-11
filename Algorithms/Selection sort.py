def check(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst
#Thuật toán này stable , nhưng vẫn có thể tối ưu thêm nếu ta gắn thêm biến True Fale
#https://cafedev.vn/thuat-toan-bubble-sort-gioi-thieu-chi-tiet-va-code-vi-du-tren-nhieu-ngon-ngu-lap-trinh/

try:
    s = input("Enter your string : ").split()
    lst = list(map(int, s))
    if len(lst) == 0 :
        print("Danh sách rỗng")
    else:
        check(lst)
        for i in lst:
            print(i, end=" ")

except:
    print("Định dạng đầu vào không hợp lệ")
