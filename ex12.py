from os import system
import random
system ('cls')

#print(random.randint(0,100))
num = random.randint(0,100)
print (num)

#o n escolhido é par ou impar
#o n escolhido é maior q 50 ou menor?

# o numero escolhido é primo?

if num%2 == 0:

    print ('é par')
else:
    print ('é impar')    

if int (num) > 50:
    print('é maior que 50')
else:
    print('é menor que')    