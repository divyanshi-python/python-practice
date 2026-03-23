s = input('enter string')
count = 0

for ch in s:
    if ch in "AEIOUaeiou":
        count += 1

print("Vowels =", count)
