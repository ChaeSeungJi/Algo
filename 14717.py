import sys
input = sys.stdin.readline



def evaluate_hand(card1, card2):
    if card1 == card2:
        return f"{card1}땡"
    else:
        sum_mod = (card1 + card2) % 10
        return f"{sum_mod}끗"


def compare_hands(young_hak_hand, opponent_hand):
    # 우선순위 맵을 수정하여 0끗에서 시작하고 각 땡의 우선순위를 1씩 증가시킵니다.
    priority = {'10땡': 20, '9땡': 19, '8땡': 18, '7땡': 17, '6땡': 16,
                '5땡': 15, '4땡': 14, '3땡': 13, '2땡': 12, '1땡': 11,
                '0끗': 1, '1끗': 2, '2끗': 3, '3끗': 4, '4끗': 5,
                '5끗': 6, '6끗': 7, '7끗': 8, '8끗': 9, '9끗': 10}
    if priority[young_hak_hand] > priority[opponent_hand]:
        return True
    else:
        return False


def calculate_winning_probability(A, B):
    deck = [x for x in range(1, 11) for _ in range(2)]  # 덱 생성
    deck.remove(A)  # 영학이의 카드 제거
    deck.remove(B)
    young_hak_hand = evaluate_hand(A, B)

    wins = 0
    total = 0

    # 남은 카드 조합을 모두 검사
    for i in range(len(deck)):
        for j in range(i + 1, len(deck)):
            opponent_hand = evaluate_hand(deck[i], deck[j])
            if compare_hands(young_hak_hand, opponent_hand):
                wins += 1
            total += 1

    probability = wins / total
    return f"{probability:.3f}"



a, b = map(int, input().split())
print(calculate_winning_probability(a, b))  
