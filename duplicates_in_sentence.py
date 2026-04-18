s = "programming"
seen=set()
dup=set()
for char in s :
    if char in seen:
        dup.add(char)
    else:
        seen.add(char)
print("duplicates characters : ",dup)
