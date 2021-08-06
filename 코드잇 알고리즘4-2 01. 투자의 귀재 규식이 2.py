# 알고리즘 연습 Level 2
# 01. 투자의 귀재 규식이 2



# 실습과제
# 100XP
# 저번 챕터에서 sublist_max 함수를 Brute Force 방식으로 작성했습니다. 이번에는 같은 문제를 Divide and Conquer 방식으로 풀어볼 텐데요. 시간 복잡도는 O(n\lg{n})O(nlgn)이 되어야 합니다.

# 이번 sublist_max 함수는 3개의 파라미터를 받습니다.

# profits: 며칠 동안의 수익이 담겨 있는 리스트
# start: 살펴볼 구간의 시작 인덱스
# end: 살펴볼 구간의 끝 인덱스
# sublist_max는 profits의 start부터 end까지 구간에서 가능한 가장 큰 수익을 리턴합니다.

# 합병 정렬을 구현할 때 merge_sort 함수를 깔끔하게 작성하기 위해 추가로 merge 함수를 작성했던 것 기억 나시나요? 마찬가지로 퀵 정렬을 구현할 때 quicksort 함수에 추가로 partition 함수를 작성했습니다. 이번에도 sublist_max 함수에 추가로 새로운 함수를 작성하면 도움이 되실 겁니다.

def find_same_number(some_list):
    # for 문의 시간복잡도 O(n)
    for i in range(1, len(some_list)):
    # python 내장 함수의 시간복잡도 O(n)
        some_list.remove(i)
    return some_list[0]


# 중복되는 수 ‘하나’만 리턴합니다.
print(find_same_number([1, 4, 3, 5, 3, 2]))
print(find_same_number([4, 1, 5, 2, 3, 5]))
print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))








def sublist_max(profits, start, end):
    # 코드를 작성하세요. 
    profits = sorted(profits)
    max_value = 0
    for i in range(len(profits)):
        if profits[i] > 0:
            max_value +=profits[i]
    return max_value

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))





#시간 복잡도 O(n)
#if element in elements_seen_so_far: #
# 리스트 if문의 경우 인덱스 값을 이용해서 탐색이 아니라, 바로 찾기 때문에 시간복잡도가 O(1)이다. 
# def find_same_number(some_list):
#     # 이미 나온 요소를 저장시켜줄 사전
#     elements_seen_so_far = {}

#     for element in some_list:
#         # 이미 나온 요소인지 확인하고 맞으면 요소를 리턴한다
#         if element in elements_seen_so_far:
#             return element

#         # 해당 요소를 사전에 저장시킨다
#         elements_seen_so_far[element] = True

# print(find_same_number([1, 4, 3, 5, 3, 2]))
# print(find_same_number([4, 1, 5, 2, 3, 5]))
# print(find_same_number([5, 2, 3, 4, 1, 6, 7, 8, 9, 3]))