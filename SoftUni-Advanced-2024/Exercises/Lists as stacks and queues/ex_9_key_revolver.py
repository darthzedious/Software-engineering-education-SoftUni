from collections import deque

bullet_price = int(input())
revolver_capacity = int(input())
bullets = deque(map(int, input().split())) #1st way to convert it.
locks = deque([int(lock) for lock in input().split()]) #2nd way to convert it.
intelligence = int(input())

bullets_in = revolver_capacity
bullets_used = 0

while bullets and locks:
    bullet = bullets.pop()
    lock = locks.popleft()
    if bullet <= lock:
        print("Bang!")
        bullets_used += 1
        bullets_in -= 1
    else:
        print("Ping!")
        bullets_used += 1
        bullets_in -= 1
        locks.appendleft(lock)
    if bullets:
        if bullets_in == 0:
            bullets_in = revolver_capacity
            print("Reloading!")

bullets_left = len(bullets)
locks_left = len(locks)

bullets_cost = bullets_used * bullet_price
money_earned = intelligence - bullets_cost

if not locks:
    print(f"{bullets_left} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {locks_left}")
