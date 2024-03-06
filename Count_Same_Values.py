values = map(float, input().split(' '))

def my_count(values, value):
    count = 0
    for x in values:
        if x == value:
            count += 1
    return  count

values_count = {}
for value in values:
    if value not in values_count:
        values_count[value] = 0

    values_count[value] += 1

for (value, count) in values_count.items():
    print(f'{value} - {count} times')