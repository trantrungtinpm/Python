def partition(lst, low, hight):
    pivot = lst[hight]
    i = low - 1

    for j in range(low, hight):
        if lst[j] <= pivot:
            i = i + 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i+1], lst[hight] = lst[hight], lst[i+1]
    return i + 1


def quicksort(lst, low, hight):
    if low < hight:
        pi = partition(lst, low, hight)
        quicksort(lst, low, pi - 1)
        quicksort(lst, pi + 1, hight)

#thuật toán này chưa stable , time complexity còn tùy thuộc vào thứ tự các số trong list ( vị trí chọn pivot )
#https://cafedev.vn/thuat-toan-quicksort-gioi-thieu-chi-tiet-va-code-vi-du-tren-nhieu-ngon-ngu-lap-trinh/


try:
    s = input("Enter your string: ").split()
    lst = list(map(float, s))
    size = len(lst)
    if size == 0 :
        print("Danh sách rỗng")
    else:
        quicksort(lst, 0, size -1)
        print(lst)
except:
    print("Vui lòng nhập các phần tử là số thực")

