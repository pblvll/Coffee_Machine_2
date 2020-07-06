original = input()
new = float(original)
y = 0

while new <= 700000:
    y += 1
    new = float(new) * 1.071

print(int(y))
