def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def print_result(names):
    for name in names:
        print(name)

# names = [
#         'Lee',
#         'Joey',
#         'Lee',
#         'Joe',
#         'Alan',
#         'Alan',
#         'Peter',
#         'Joey',
# ]

unique_names = set()
for name in names:
    unique_names.add(name)
print_result(unique_names)
