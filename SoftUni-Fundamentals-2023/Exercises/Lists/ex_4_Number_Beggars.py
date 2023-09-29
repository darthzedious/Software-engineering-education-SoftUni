list_of_numbers = input().split(", ")
count_of_beggars = int(input())
list_of_numbers_as_digit = []
for i in list_of_numbers:
    list_of_numbers_as_digit.append(int(i))
final_list = []
start_index = 0
while start_index < count_of_beggars:
    sum_for_current_beggar = 0
    for i in range(start_index, len(list_of_numbers_as_digit), count_of_beggars):
        sum_for_current_beggar += list_of_numbers_as_digit[i]
    final_list.append(sum_for_current_beggar)
    start_index += 1
print(final_list)
and int(cmnd[2]) in gifts