str = input()

# -가 있는지 없는지 check 

if str.find("-")!=-1:

    list = str.split('-')

    l = [sum(map(int,i.split('+'))) if i.find('+') else int(i) for i in list]

    result = l[0]

    for i in l[1:]:
        result-=i;

    print(result) 
        
else:
    
    print(sum(map(int,str.split('+'))))