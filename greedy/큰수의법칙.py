N=5
M=8
K=3
arr=[2, 4, 5, 4, 6]

arr=sorted(arr, reverse=True)
res=0
cnt=0
idx=0

for a in range(0, M):
    cnt+=1
    if cnt%(K+1)!=0:
        res+=arr[0]
    else:
        res+=arr[1]
print(res)
    
    
