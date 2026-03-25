a= [1,2,3,4]
b= [3,4,5,6]
b_set=set(b)
res=[]
for i in a:
  if i in b_set:
    res.append(i)
print (res)
    
