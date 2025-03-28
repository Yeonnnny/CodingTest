from datetime import datetime, timedelta
import heapq

def solution(book_time):
    # 1. 문자열을 datetime 객체로 변환하면서 종료시간에 청소시간 10분 더해줌
    times = []
    for start, end in book_time:
        start_time = datetime.strptime(start, "%H:%M")
        end_time = datetime.strptime(end, "%H:%M") + timedelta(minutes=10)
        times.append((start_time, end_time))
    
    # 2. 시작 시간 기준으로 정렬
    times.sort()

    # 3. 최소 힙 (사용 중인 방들의 종료시간을 저장)
    rooms = []

    for start, end in times:
        # 가장 빨리 끝나는 방부터 체크 (rooms[0]은 가장 이른 종료 시간)
        if rooms and rooms[0] <= start:
            # 기존 방 재사용 가능 → 종료시간 갱신
            heapq.heappop(rooms)
        # 새 방 추가 or 기존 방 종료시간 갱신
        heapq.heappush(rooms, end)

    # 4. heap에 남아있는 방 개수가 필요한 최소 객실 수
    return len(rooms)
