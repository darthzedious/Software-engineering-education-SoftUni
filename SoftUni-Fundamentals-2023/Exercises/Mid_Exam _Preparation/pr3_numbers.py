sequence_of_integers = list(map(int, input().split()))
final_list = []
greater_than_average = [num for num in sequence_of_integers if num > sum(sequence_of_integers) // len(sequence_of_integers)]
sorted_numbers = sorted(greater_than_average)
sorted_backwards = list(map(str, sorted(sorted_numbers, reverse=True)))
top_five = sorted_backwards[:5]
if len(sequence_of_integers) > 1:
    for num in range(len(top_five)):
        final_list.append(sorted_backwards[num])
    print(" ".join(final_list))
else:
    print("No")
