# tc 1
N=3
M=3
arr=[[3, 1, 2], [4, 1, 4], [2, 2, 2]]

# tc 2
# N=2
# M=4
# arr=[[7, 3, 1, 8], [3, 3, 3, 4]]

mvalue = 0
for i in range(0, N):
    arr[i]=sorted(arr[i])
    if mvalue < arr[i][0]:
        mvalue=arr[i][0]

print(mvalue)