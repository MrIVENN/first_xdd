a = int(input())
first_dig = 0
last_dig = a % 10
while a:
    if a < 10:
        first_dig = a
    a //= 10
sum = first_dig + last_dig
print(sum)