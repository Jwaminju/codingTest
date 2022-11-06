S="02984"

idx=1
res=0
a = int(S[0]) 

for s in S[:len(S)-1]:
    b = int(S[idx])
    if a+b > a*b:
        res=a+b
    else:
        res=a*b
    a=res
    idx+=1

print(res)
