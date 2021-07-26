# #Lesson_typepassed_checker
# Greedy Algorithm
# 06. 최대 곱 구하기

# 10. 수강 신청
# 실습과제
# 100XP
# def max_product(card_lists):
#     # 코드를 작성하세요.


# # 예시
# test_cards = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
# print(max_product(test_cards))
# 여럿이서 카드 게임을 하고 있는데, 각 플레이어는 3장의 카드를 들고 있습니다. 위의 경우 첫 번째 플레이어는 1, 2, 3을 들고 있고, 두 번째 플레이어는 4, 6, 1을 들고 있고, 세 번째 플레이어는 8, 2, 4를 들고 있는 거죠.

# 함수 max_product는 한 사람당 카드를 하나씩 뽑아서 모두 곱했을 때 가능한 최대 곱을 리턴합니다. max_product를 Greedy Algorithm 방식으로 구현해 보세요.

def max_product(card_lists):
    max_value = 1
    for i in card_lists:
        max_value *= max(i)
    return max_value 

        

# 테스트
test_cards1 = [[1, 6, 5], [4, 2, 3]]
print(max_product(test_cards1))

test_cards2 = [[9, 7, 8], [9, 2, 3], [9, 8, 1], [2, 8, 3], [1, 3, 6], [7, 7, 4]]
print(max_product(test_cards2))

test_cards3 = [[1, 2, 3], [4, 6, 1], [8, 2, 4], [3, 2, 5], [5, 2, 3], [3, 2, 1]]
print(max_product(test_cards3))

test_cards4 = [[5, 5, 5], [4, 3, 5], [1, 1, 1], [9, 8, 3], [2, 8, 4], [5, 7, 4]]
print(max_product(test_cards4))


# def max_product(card_lists):
#     cache = []
#     # 코드를 작성하세요.
#     max_value = 1
#     while len(cache) < len(card_lists):
#         if len(card_lists) < 2:
#             for i in card_lists:
#                 cache.append(max(i))

#         return max_product(card_lists[:-1])
    
#     for i in cache:
#         max_value *= i

#     for i in card_lists[-1]:
#         max_value *= i
    
#     return max_value