a = int(input())
dig = 0
summ = 0
summ1 = 0
mult = 1
quan = 0
first_dig = 0
last_dig = a % 10
while a != 0:
    digital = a % 10
    summ += digital
    dig += 1
    digital1 = a % 10
    mult *= digital1
    digital2 = a % 10
    quan += 1
    summ1 += digital2
    if a < 10:
        first_dig = a
    a //= 10
arith_mean = summ1 / quan
summ2 = first_dig + last_dig



print(summ)
print(dig)
print(mult)
print(arith_mean)
print(first_dig)
print(summ2)