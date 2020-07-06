time = int(input())
reference = 10.5
if (reference + time) < 0:
    print("Monday")
elif (reference + time) > 24:
    print("Wednesday")
else:
    print("Tuesday")
