from os import system
import random
system ('cls')

num1 = random.randint(0,100)
num2 = random.randint(0,100)
num3 = random.randint(0,100)

print (num1)
print (num2)
print (num3)

if num1 > num2 and num1 > num3:
    print(f'{num1} é o maior')

elif num2 > num1 and num2 > num3:
    print(f'{num2} é o maior')
else:
    print(f'{num3} é o maior')
