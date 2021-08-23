# 4 задание
def count(number):
    k = 0
    for i in range(1, number):
        if number % i == 0:
            k = k + 1
    return k


def biggest_number(a, b):
    k = 0
    l = list()
    m = list()
    for i in range(a, b - 1):
        if k < count(i):
            k = count(i)
    for i in range(a, b - 1):
        if count(i) == k:
            l.append(i)
            m.append(k)
    return list(zip(l, m))




a = int(input())
b = int(input())
print(biggest_number(a, b))





# 5 задание
def unique(a):
    for i in range(0, len(a) - 1):
        for j in range(i + 1, len(a)):
            if int(a[i]) == int(a[j]):
                return False
    return True

a = input().split(" ")
print(unique(a))





# 6 задание
def empty(*params):
    str = params[0]
    for i in (1, len(params)-1):
        str = set(params[i]) & set(str)
    if not str:
	 return True
    else:
	 return False


a = input().split(" ")
b = input().split(" ")
c = input().split(" ")
if empty(a, b, c) == True:
    print(“True”)
else:
    print(“False”)







# треугольник паскаля
def current_row(n):
    a = []
    for i in range(0, n):
        if i == 0 or i == n - 1:
            a.append(1)
        else:
            c_row = current_row(n - 1)
            a.append(c_row[i - 1] + c_row[i])
    return a

def pascal(n):
    a = []
    for i in range(0, n):
          a.append(current_row(i + 1))
    return a

n = int(input())
l = pascal(n)
for i in range(0, n):
    print(l[i])



