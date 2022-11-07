def solution(food_times, k):
    
    l=len(food_times)
    answer = -1

    sub=min(min(food_times), k//l)
    idx=0
    
    for i, v in enumerate(food_times):
        food_times[i]-=sub
    
    k-=sub*l

    a=0
    while True:
        if a==k:
            answer=-1
            for i, v in enumerate(food_times[idx%l:]+food_times[:idx%l]):
                if v != 0:
                    answer=idx%l+1
                    break
                idx+=1
            break
        if food_times[idx%l]!=0:
            food_times[idx%l]-=1
            a+=1
        idx+=1
        
    
    return answer