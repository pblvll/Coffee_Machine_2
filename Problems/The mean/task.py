numbers = 0
divisor = 0
while True:
    n = input()
    if n != ".":
        divisor += 1
        numbers = numbers + int(n)
    else:
        print(float(numbers / divisor))
        break
