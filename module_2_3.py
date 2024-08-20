my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

l = 0
if l < len(my_list):
    while my_list[l] >= 0:
        if my_list[l] == 0:
            l += 1
            continue
        print(my_list[l])
        l += 1
