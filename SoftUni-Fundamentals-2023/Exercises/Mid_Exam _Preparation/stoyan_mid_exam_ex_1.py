from math import floor
biscuit_per_worker_for_day = int(input())
workers_count = int(input())
enemy_biscuits_for_30_days = int(input())
month_production = 0
prod_per_day = biscuit_per_worker_for_day * workers_count
for i in range(1, 30+1):
    if i % 3 == 0:
        month_production += floor(prod_per_day * 0.75)
    else:
        month_production += floor(prod_per_day)
print(f"You have produced {month_production} biscuits for the past month.")
percent = ((enemy_biscuits_for_30_days - month_production) / enemy_biscuits_for_30_days) * 100
if month_production > enemy_biscuits_for_30_days:
    print(f"You produce {abs(percent):.2f} percent more biscuits.")
elif month_production < enemy_biscuits_for_30_days:
    print(f"You produce {abs(percent):.2f} percent less biscuits.")
