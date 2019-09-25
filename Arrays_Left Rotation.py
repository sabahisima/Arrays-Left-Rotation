def rotLeft(n, d):
    list = []
    rotated_list = []
    for i in range(1, n+1):
        list.append(i)
    print(list)
    for j in range(len(list)):
        if len(rotated_list) == len(list):
            print(rotated_list)
            break
        elif j < len(list)-d:
            rotated_list.append(list[j+d])
        else:
            for k in range(d):
                rotated_list.append(list[k])

rotLeft(5, 3)