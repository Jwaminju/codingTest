# tc 2 
# N=8
# M=5
# arr=[1, 5, 4, 3, 2, 4, 5, 2]

# tc 2
N=8
M=5
arr=[1, 5, 4, 3, 2, 4, 5, 2]

def comb(arr, n):
    result=[]
    if n >len(arr):
        return result
    if n==1:
        for a in arr:
            result.append([a])
    elif n>1:
        for i in range(len(arr)-n+1): # 5-2+1=4
            for j in comb(arr[i+1:], n-1):
                result.append([arr[i]]+j)
    return result

res=0
for set in comb(arr, 2):
    if set[0]==set[1]:
        pass
    else:
        res+=1

print(res)

