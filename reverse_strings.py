text = 'I love Python'

s = []

for ch in text:
    s.append(ch)

result = ''

while s:
    result += s.pop()

print(result)