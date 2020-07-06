output = []
while True:
    lines = input()
    if lines == ".":
        break
    output.append(float(lines))
print(min(output))
