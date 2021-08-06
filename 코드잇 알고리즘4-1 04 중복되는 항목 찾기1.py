# 알고리즘 연습 Level 1
# 04. 중복되는 항목 찾기 I



# (N + 1)의 크기인 리스트에, 1부터 N까지의 임의의 자연수가 요소로 할당되어 있습니다. 그렇다면 어떤 수는 꼭 한 번은 반복되겠지요.

# 예를 들어 [1, 3, 4, 2, 5, 4]와 같은 리스트 있을 수도 있고, [1, 1, 1, 6, 2, 2, 3]과 같은 리스트가 있을 수도 있습니다. (몇 개의 수가 여러 번 중복되어 있을 수도 있습니다.)

# 이런 리스트에서 반복되는 요소를 찾아내려고 합니다.

# 중복되는 어떠한 수 ‘하나’만 찾아내도 됩니다. 즉 [1, 1, 1, 6, 2, 2, 3] 예시에서 1, 2를 모두 리턴하지 않고, 1 또는 2 하나만 리턴하게 하면 됩니다.

# 중복되는 수를 찾는 시간 효율적인 함수를 설계해보세요.

#시간복잡도가 remove의 내장함수가 O(n)이기 때문에 O(n*n)이 든다. 
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





def sublist_max(profits, start, end):
    # 코드를 작성하세요. 
    mid = (start + end) //2
    
    left = 0
    for i in range(start, mid+1):
        if profits[i] > 0:
            left += profits[i]
            
    right = 0
    for i in range(mid+1, end+1):
        if profits[i] > 0:
            right += profits[i]
    
    return left + right

# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))



def sublist_max(profits, start, end):
# 코드를 작성하세요. 
    max_value = 0
    for i in range(len(profits)):
        if profits[i] > 0:
                max_value +=profits[i]
    return max_value
        
	# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))
