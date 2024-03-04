expression = '1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5'

s = []

for i in range(len(expression)):
    ch = expression[i]
    if ch == '(':
        s.append(i)
    elif ch == ')':
        j = s.pop()
        print(expression[j:i+1])