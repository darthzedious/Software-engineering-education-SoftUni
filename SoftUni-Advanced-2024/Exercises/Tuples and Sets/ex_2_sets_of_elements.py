n, m = [int(num) for num in input().split()]

col_1 = set()
col_2 = set()
for _ in range(n):
    col_1.add(int(input()))
for _ in range(m):
    col_2.add(int(input()))

answer = col_1.intersection(col_2)
print(*answer, sep="\n")
