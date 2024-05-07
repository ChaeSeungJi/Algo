def BFS(graph, S): # BFS 정의
    visited = [False]*(len(graph)+1) # 방문 처리를 위해 생성
    queue = []
    queue.append(S)
    visited[S] = True # 현재 노드 방문처리
    while queue :
        a = queue.pop(0) #큐에 순차적으로 삽입
        print(a, end = ' ')
        for i in graph[a]: #방문하지 않은 인접 노드들을 큐에 삽입
            if not visited[i] : 
                queue.append(i)
                visited[a] = True

graph = [[],[2,3,4],[],[],[5,6],[],[]]
BFS(graph,1)
출처: https://edder773.tistory.com/35 [개발하는 차리의 공부 일기:티스토리]
