from datetime import datetime, timedelta
import heapq

def solution(book_time):
    times = []
    for start, end in book_time:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M") + timedelta(minutes=10)
        times.append((start_time, end_time))

    times.sort()

    rooms = [] # 종료 시간 저장(종료+청소10분)

    for start, end in times:
        if rooms and rooms[0] <= start:  # 가장 빨리 끝나는 방부터 체크
            heapq.heappop(rooms) 
        heapq.heappush(rooms, end)

    return len(rooms)
