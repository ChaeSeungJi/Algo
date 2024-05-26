# 그리디 알고리즘 (Greedy Algorithm)

## 개념
그리디 알고리즘은 매 선택에서 지금 이 순간 최적의 해답을 선택하는 방식으로 문제를 해결하는 알고리즘입니다. 
이 방식은 전체를 고려하지 않고, 각 단계에서 최선의 선택을 함으로써 최종적인 해결책에 도달합니다. 그리디 알고리즘은 최적해를 보장하지 않는 경우가 많지만, 특정 문제에서는 매우 효과적이고 빠른 해결책을 제공합니다.

## 예시: 동전 문제
- 문제 설명: 주어진 동전들을 최소 개수로 사용하여 특정 금액을 만드는 문제.
- 입력: 사용 가능한 동전의 종류 배열 coins, 만들어야 할 금액 amount.
- 출력: 필요한 최소 동전의 개수.


```Sort `coins` in descending order.
Initialize `coin_count` to 0.
For each coin in `coins`:
   Calculate how many times the current coin fits into `amount`.
   Reduce `amount` by the total value taken by the current coin.
   Increment `coin_count` by the number of coins used.
If `amount` is 0 after the loop, return `coin_count`.
If not, return -1 (not possible to make the amount).'''

# 브루트포스 알고리즘 (Brute Force Algorithm)

## 개념
브루트포스 알고리즘, 또는 완전 탐색 알고리즘은 가능한 모든 경우의 수를 탐색하여 문제의 해답을 찾는 방법입니다. 
이 방법은 모든 가능성을 체크하기 때문에 해답을 찾을 수 있는 가장 확실한 방법이지만, 경우의 수가 많을 때는 비효율적일 수 있습니다.

## 예시: 순열 생성
- 문제 설명: 주어진 배열의 모든 순열을 생성하는 문제.
- 입력: 배열 arr.
- 출력: 배열 arr의 모든 순열.

```Initialize `perm_list` to an empty list.
Define a function `permute` with parameters `current_permutation` and `elements`:
   a. If `current_permutation` length equals `arr` length:
      - Append `current_permutation` to `perm_list`.
   b. Else:
      - For each element in `elements`:
        i. Remove element from `elements`.
        ii. Call `permute` with element added to `current_permutation`.
        iii. Restore element to `elements`.
Call `permute` with an empty list and `arr`.
Return `perm_list`.```
