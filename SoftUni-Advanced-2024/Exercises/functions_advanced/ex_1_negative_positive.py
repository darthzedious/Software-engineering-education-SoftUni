def find(args):
    negative = []
    positive = []
    conclusion = ""

    for num in args:
        if num < 0:
            negative.append(num)
        else:
            positive.append(num)

    if abs(sum(negative)) > sum(positive):
        conclusion = "The negatives are stronger than the positives"
    else:
        conclusion = "The positives are stronger than the negatives"

    return f"{sum(negative)} \n{sum(positive)} \n{conclusion}"


print(find([int(x) for x in input().split()]))
