# BFS (Breadth-First Search, 너비 우선 탐색)
## 개념
너비 우선 탐색(BFS)은 그래프의 가장 가까운 노드부터 차례대로 탐색하는 방법입니다. BFS는 큐(Queue)를 사용하여 구현하며, 시작 정점에서 가까운 정점을 먼저 방문하고 멀리 떨어진 정점을 나중에 방문하는 순서로 진행됩니다. BFS는 그래프의 모든 노드를 방문하며, 최단 경로 문제 등에 사용됩니다.

```
Initialize a queue and enqueue the starting node.
Mark the starting node as visited.
While the queue is not empty:
   a. Dequeue an element from the queue and call it `current`.
   b. For each neighbor of `current`:
      i. If the neighbor has not been visited:
         - Mark the neighbor as visited.
         - Enqueue the neighbor.
Repeat until the queue is empty.

```


# DFS (Depth-First Search, 깊이 우선 탐색)

## 개념
깊이 우선 탐색(DFS)은 그래프의 깊은 부분을 우선적으로 탐색하는 방법입니다. DFS는 스택(Stack)을 사용하거나 재귀 함수를 통해 구현할 수 있으며,
방문한 노드를 차례로 탐색하다가 더 이상 탐색할 곳이 없으면 이전 분기점으로 돌아가 다른 경로를 탐색하는 방식을 사용합니다. DFS는 모든 노드를 방문할 필요가 있는 문제, 경로의 가능성을 전체적으로 탐색해야 할 때 유용합니다.


```
Initialize an empty stack and push the starting node.
While the stack is not empty:
   a. Pop the top element from the stack and call it `current`.
   b. If `current` has not been visited:
      i. Mark `current` as visited.
      ii. For each neighbor of `current`:
         - If the neighbor has not been visited:
           - Push the neighbor onto the stack.
```
