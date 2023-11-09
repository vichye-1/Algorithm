from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = [cities[i].upper() for i in range(len(cities))]
    queue = deque([])
  
    if cacheSize == 0:
        return len(cities) * 5
      
    for city in cities:
        if city in queue:
            answer += 1
            queue.remove(city)
            queue.append(city)
        else:
            if len(queue) >= cacheSize:
                answer += 5
                queue.popleft()
                queue.append(city)
            else:
                answer += 5
                queue.append(city)
              
    return answer
