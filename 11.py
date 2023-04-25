a = int(input())
mult = 1
while a != 0:
    digital = a % 10
    mult *= digital
    a //= 10
print(mult)