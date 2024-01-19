array=list(map(int, input().split()))

for i in range(3):
    min=1000001
    for j in range(i,3):
        if min > array[j]:
            min=array[j]
            index=j
        j+=1   
    array[i],array[index]=array[index],array[i]

print(*array)
