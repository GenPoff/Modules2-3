my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = 0
while my_list[x] > 0 and x < len(my_list):
    print(my_list[x])
    x += 1
    if my_list[x] == 0:
        x += 1
