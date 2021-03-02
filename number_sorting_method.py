def sort_list(list):
    for i in range(len(list)):
        current = list[i]
        j = i - 1
        while(j >= 0 and current < list[j]):
            list[j], list[j + 1] = list[j + 1], list[j]
            j -= 1

        list[j+1] = current
    print(list)