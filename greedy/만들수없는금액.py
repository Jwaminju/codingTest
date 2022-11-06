
N=5
arr=[3, 2, 1, 1, 9]
arr=sorted(arr)

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


result=[]
for i in range(1, N+1):
    comb_set = comb(arr, i)

    for set in comb_set:
        sum=0
        if len(set)==1:
            sum=set[0]
        else:
            for a in set:
                sum+=a
        result.append(sum)
    
result=sorted(result)

idx=0
for k in range(len(result)-1):
    
    if result[idx] == result[idx+1]:
        # 왜 이 안에서 idx+=1하면 안되지? : 같지도 않고, 1, 2, 연속되어 있는 수면 idx+=1 이 안되니까 
        pass
    elif result[idx] + 1 != result[idx+1]:
        break
    idx+=1

print(result[idx]+1)

        


    
    