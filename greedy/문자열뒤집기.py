S="0001100"

idx=1
group=0
for s in S[:len(S)-1]:
    if S[idx-1] != S[idx]:
        group+=1
    idx+=1

print(group-1)