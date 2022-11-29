# tc 2 
# N=8
# M=5
# arr=[1, 5, 4, 3, 2, 4, 5, 2]

# tc 2
N=8
M=5
arr=[1, 5, 4, 3, 2, 4, 5, 2]

weigth=[0]*11
for i in arr:
    weigth[i] += 1

result=0
for i in range(1, M+1):
    N -= weigth[i] 
    result += weigth[i]*N

print(result)