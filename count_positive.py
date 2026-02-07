def positive(n):
    count=0
    for i in n:
        if i>0:
         count+=1
    return count
li=[1,2,3,5,7,5,56,5,655,-9,-9,98,0,-8,-7,-6]
print ("original list",li)
print("positive number in list",positive(li))
