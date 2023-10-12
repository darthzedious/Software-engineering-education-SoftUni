number_list = list(map(int, input().split(", ")))
found_index_or_not = map(lambda x: x if number_list[x] % 2 == 0 else "no",
                         range(len(number_list)))
even_index = list(filter(lambda a: a != "no", found_index_or_not))
print(even_index)
