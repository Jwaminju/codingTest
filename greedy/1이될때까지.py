N=25
K=3

cnt=0
while N!=1:
    if N%K==0:
        N=N//K
    else:
        N-=1
    cnt+=1
print(cnt)