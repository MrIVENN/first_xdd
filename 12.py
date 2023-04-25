a = int(input())
sum = 0
quan = 0
while a != 0:
    digital = a % 10
    quan += 1
    sum += digital
    a //= 10
arith_mean = sum / quan
print(arith_mean)