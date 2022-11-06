N=5
arr=[2, 3, 1, 2, 2]

arr=sorted(arr)

res=0
idx=0
temp=arr
while True:
    if len(temp) >= temp[0]:
        if temp[temp[0]-1] <= temp[0]: 
            res+=1
            temp=temp[temp[0]:]
        else:
            break
    else: 
        break
print(res)
