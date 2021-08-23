# 1 задание
x=int(input())
if x % 4 == 0:
    if (x // 100) % 4 != 0:
        print('Год невисокосный')
    else:
        print('Год високосный')
else:
    print('Год невисокосный')




# 2 задание
x=int(input())
x_tmp = x
x_tmp2 = x
sum=0
k=0
while(x_tmp != 0):
    x_tmp=x_tmp//10
    k+=1
while(x_tmp2!=0):
    sum = sum + (x_tmp2%10)**k
    x_tmp2 //= 10
if (sum == x):
    print('Число является числом Армстронга')
else:
    print('Число не является числом Армстронга')

for x in range(1, 1000):
    x_tmp = x
    x_tmp2 = x
    sum=0
    k=0
    while(x_tmp != 0):
        x_tmp=x_tmp//10
        k+=1
    while(x_tmp2!=0):
        sum = sum + (x_tmp2%10)**k
        x_tmp2 //= 10
    if (sum == x):
        print(x,'Число является числом Армстронга')
    else:
        print(x,'Число не является числом Армстронга')




# 3 задание
def fibonacci(number):     #фунция возвращает номер числа в пос-ти
    k = 2
    x = 1
    x2 = 1
    x3 = 1
    if number == 1:
        return 2
    if number == 2:
        return 3
    while number != x :
        x = x2+x3
        x3 = x2
        x2 = x
        k += 1
        if k == 30:
            return 1
    return k


flag = 0
sequence = []
x = int(input())
while x != 0:
    sequence.append(x)
    x = int(input())
print(sequence)
m=0
if sequence[0] == 1:
    if sequence[1] == 1:
        m = 1
k = 1
k1 = 2
for i in range(m, len(sequence)-1):    #если число оказалось тем же ли более 
    k = fibonacci(sequence[i])    #ранним, то это не пос-ть
    k1 = fibonacci(sequence[i + 1])
    if flag == 1:
        break
    if k1 <= k:
        flag = 1
        print('Это не последовательность Фибоначчи')
if flag == 0:
    print('Это последовательность фибоначчи')






# 4 задание 
def digit(number):  #вывод number магического числа
    digit = 1
    temp = digit
    i = 0
    sum = 0
    while i != number:
        digit += 1
        temp = digit
        while temp != 0:
            sum += temp % 10
            temp //= 10
        if sum == 10:
            i += 1
        sum = 0
    return digit


x=int(input())
while(x > 10000 or x < 1):
    print('Граница от 1 до 10000')
    x = int(input())
print(digit(x))


