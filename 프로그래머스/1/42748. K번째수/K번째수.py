# array : 길이, 원소 (1이상100이하)
# command : 2차원 배열 ex) [[i,j,k],[i,j,k],...] 길이 : 1이상50이하, 각 원소의 길이 : 3
# i: 시작, j:끝, k : 정렬 후 k번째

def solution(array, commands):
    answer = []
    for col in range(len(commands)):
        i = commands[col][0]
        j = commands[col][1]
        k = commands[col][2]
        
        arr = array[i-1:j];
        # 정렬
        for n in range(len(arr)):
            for m in range(n+1,len(arr)):
                if(arr[n]>arr[m]):
                    arr[n],arr[m] = arr[m],arr[n]

        answer.append(arr[k-1])
                
    return answer