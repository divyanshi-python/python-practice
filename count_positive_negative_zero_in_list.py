li=[5,-2,8,-1,0]
neg_count=0
pos_count=0
zero_count=0
for i in li:
    if i > 0:
        pos_count+=1
    elif i < 0 :
        neg_count+=1
    else:
        zero_count+=1
print("positive = ",pos_count)
print("negative = ",neg_count)
print("zero = ",zero_count)
