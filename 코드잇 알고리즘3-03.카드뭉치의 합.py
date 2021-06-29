# def max_product(left_cards, right_cards):
#     max = []
#     for i in range(len(left_cards)):
        
#         for j in range(len(right_cards)):
#             values = left_cards[i]*right_cards[j]
#             max.append(values)
#     max.sort()
#     return max[-1]

def max_product(left_cards, right_cards):
    # 현재까지 최댓값을 담기 위한 변수
    # 처음에는 임시로 각 리스트의 첫 번째 요소의 곱으로 설정
    max_product = left_cards[0] * right_cards[0]
    
    # 가능한 모든 조합을 보기 위한 중첩 반복문
    for left in left_cards:
        for right in right_cards:
            # 현재까지의 최댓값 값과 지금 보고 있는 곱을 비교해서 더 큰 값을 최댓값 변수에 담아준다
            max_product = max(max_product, left * right)
    print(max_product)

    # 찾은 최댓값을 리턴한다            
    return max_product

print(max_product([1, 6, 5], [4, 2, 3]))

    
    
# 테스트

