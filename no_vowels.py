text = 'ILOvePython'

vowels = {'a', 'o', 'u', 'e', 'i'}
vowels = vowels.union(x.upper() for x in vowels)
# [vowels .add(x.upper()) for x in list(vowels)]


text = input()
result = [ch for ch in text if ch not in vowels]
print(''.join(result))
