chars = ['a', 'b', 'c', 'a']

result = {}

for ch in chars:
    result[ch] = ord(ch)
print(result)

result = {ch: ord(ch) for ch in chars}
print(result)