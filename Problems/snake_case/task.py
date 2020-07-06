upper = input()
word = ""
for char in upper:
    if char.islower():
        word = word + char
    elif char.isupper():
        word = word + '_' + char.lower()
print(word)
