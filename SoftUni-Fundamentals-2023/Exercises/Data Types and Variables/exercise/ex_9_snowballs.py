number_of_snowballs = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0
for snowballs in range(1, number_of_snowballs + 1):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())
    value = int(weight_of_the_snowball / time_needed) ** quality
    if value > max_value:
        max_value = value
        max_weight = weight_of_the_snowball
        max_time = time_needed
        max_quality = quality
print(f"{max_weight} : {max_time} = {max_value} ({max_quality})")
