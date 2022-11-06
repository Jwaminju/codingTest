N=5
M=8
K=3
arr=[2, 4, 5, 4, 6]
arr=sorted(arr, reverse=True)

first = int((M / (K+1)))*K + M % (K+1)
second = M-first

res = arr[0]*first + arr[1]*second
print(res)