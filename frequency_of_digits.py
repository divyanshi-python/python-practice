data=[12,45,67,23,45,90,45,12,67]
freq={}
for i in data:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
print(freq)
