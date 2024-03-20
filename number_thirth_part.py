from numbersystem import decimalToBinary, decimalToHexa
from termcolor import colored
from pyfiglet import figlet_format

text = figlet_format("Python", font="isometric1")
print(text)

text = colored('Hello World!', 'red', attrs=['bold', 'underline'])
print(text)

x = 1555
print(x)
print(decimalToBinary(x))
print(decimalToHexa(x))



