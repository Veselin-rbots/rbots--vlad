text = input()

symbols = {}

for char in text:
    symbols[char] = text.count(char)

sorted_data = sorted(symbols)
# def sorted_data(x):
#     return x[0]


for key in sorted_data:
    print(f'{key}: {symbols[key]} time/s')