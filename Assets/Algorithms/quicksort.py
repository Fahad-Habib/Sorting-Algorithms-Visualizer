def quickSort(data_list, first, last):
    if first < last:
        split_point = partition(data_list, first, last)

        quickSort(data_list, first, split_point - 1)
        quickSort(data_list, split_point + 1, last)


def partition(data_list, first, last):
    pivot_value = data_list[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and data_list[left_mark] <= pivot_value:
            left_mark += 1

        while data_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            data_list[left_mark], data_list[right_mark] = data_list[right_mark], data_list[left_mark]

    data_list[first], data_list[right_mark] = data_list[right_mark], data_list[first]

    return right_mark


l = [x for x in range(10, -1, -1)]
quickSort(l, 0, len(l) - 1)
print(l)

