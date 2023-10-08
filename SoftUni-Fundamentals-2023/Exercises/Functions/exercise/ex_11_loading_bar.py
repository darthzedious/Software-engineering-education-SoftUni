def loading_bar(number: int):
    if number == 100:
        return "100% Complete!" "\n" "[%%%%%%%%%%]"
    loaded_percent = number // 10
    return f"{number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number_divisible_by_10 = int(input())
print(loading_bar(number_divisible_by_10))
