add = 0
sqr_add = 0
while True:
    n = int(input())
    add += n
    sqr_add += (n * n)
    if add == 0:
        print(sqr_add)
        break
