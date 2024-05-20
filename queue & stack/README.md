# 큐와 스택

## 스택 (Stack)

### 정의
스택은 LIFO(Last In, First Out) 원칙을 따르는 자료 구조이다. 즉, 마지막에 삽입된 데이터가 먼저 제거된다. 스택은 주로 함수 호출, 실행 취소 기능 등에서 사용된다.

### 주요 연산
- **push(item)**: 스택의 최상단에 요소를 추가.
- **pop()**: 스택의 최상단에서 요소를 제거하고 반환.
- **peek()**: 스택의 최상단에 있는 요소를 반환하되 제거하지는 않는다.
- **isEmpty()**: 스택이 비어있는지 확인.
- **size()**: 스택에 있는 요소의 개수를 반환.

### 코드 예시
```python
K = int(input())  # 정수 K 입력받기
stack = []        # 정수를 저장할 스택

for _ in range(K):
    num = int(input())  # 정수 입력받기
    
    if num == 0:  # 입력된 정수가 0이라면
        stack.pop()  # 스택에서 가장 최근에 쓴 수를 지우기
    else:
        stack.append(num)  # 0이 아닌 다른 정수일 경우 스택에 추가

# 스택에 남아있는 모든 수를 더해서 출력
print(sum(stack))


# 큐 (Queue)

## 정의
큐는 FIFO(First In, First Out) 원칙을 따르는 자료 구조이다. 즉, 먼저 삽입된 데이터가 먼저 제거된다. 큐는 주로 작업 예약, 대기열 관리 등에서 사용된다.

## 주요 연산
- **enqueue(item)**: 큐의 끝에 요소를 추가.
- **dequeue()**: 큐의 앞에서 요소를 제거하고 반환.
- **peek()**: 큐의 앞에 있는 요소를 반환하되 제거하지는 않는다
- **isEmpty()**: 큐가 비어있는지 확인.
- **size()**: 큐에 있는 요소의 개수를 반환.

## 파이썬으로 큐 구현 예시
큐는 파이썬의 `collections.deque`를 사용하여 효율적으로 구현할 수 있다.

```python
from collections import deque

queue = deque()  # 큐 생성

# 큐에 요소 추가
queue.append(1)  # enqueue 1
queue.append(2)  # enqueue 2
queue.append(3)  # enqueue 3

# 큐에서 요소 제거
print(queue.popleft())  # dequeue, 출력: 1
print(queue.popleft())  # dequeue, 출력: 2

# 큐의 앞에 있는 요소 확인
print(queue[0])  # peek, 출력: 3

# 큐가 비어있는지 확인
print(len(queue) == 0)  # isEmpty, 출력: False

# 큐에 있는 요소의 개수
print(len(queue))  # size, 출력: 1
