
cnt=0

while True:
    cnt +=1
    L,P,V=map(int, input().split())
    if L==0 & P==0 & V==0:
        break    
    n=V//P
    a=V%P    

    if a>L:
        total=n*L+L
    else:
        total=n*L+a

    print("Case ",cnt,": ",total, sep='')

