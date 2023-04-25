a = int(input())
summ = 0
while a != 0:
    digital = a % 10
    summ += digital
    a //= 10
print(summ)