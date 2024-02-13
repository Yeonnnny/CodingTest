def solution(progresses, speeds):
    
    last_day=[]
    for i in range(len(progresses)):
        last_val = 100-progresses[i] 
        last = last_val//speeds[i]+1 if (last_val%speeds[i]!=0) else last_val//speeds[i]
        last_day.append(last)

    ans=[]
    cnt=1
    kijun=0
    for i in range(1,len(last_day)):

        if last_day[i]<=last_day[kijun]:
            cnt+=1
        else:
            ans.append(cnt)
            kijun=i
            cnt=1

        if i==len(last_day)-1:
            ans.append(cnt)

    return ans