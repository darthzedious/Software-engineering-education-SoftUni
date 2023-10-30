def linear_search(input_list, target):
    left = 0
    right = len(input_list) - 1

    while left <= right:
        middle_index = len(input_list) // 2
        middle_element = input_list[middle_index]

        if middle_element == target:
            return middle_index
        if target > middle_element:
            left = middle_element + 1
        else:
            right = middle_element - 1


my_list = [1, 3, 5, 7, 9, 11]
target = 7
print(linear_search(my_list, target))
