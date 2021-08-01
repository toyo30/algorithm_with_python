# 알고리즘 연습 Level 1
# 02. 거듭 제곱 빠르게 계산하기

# profile_photo

# 알고리즘의 정석
# 토픽 4
# 문제 해결 능력 기르기
# 1/12 완료

# 알고리즘 연습 Level 1
# 알고리즘 연습 Level 2
# 알고리즘 연습 Level 3
# 01. 중복되는 항목 찾기 II
# 02. 리스트 항목 합 탐색
# 03. 강남역 폭우 II
# 실습과제
# 거듭 제곱을 계산하는 함수 power를 작성하고 싶습니다. power는 파라미터로 자연수 x와 자연수 y를 받고, x^yx 
# y
#  를 리턴합니다.

# 가장 쉽게 생각할 수 있는 방법은 반복문으로 단순하게 xx를 yy번 곱해 주는 방법입니다.

# def power(x, y):
#     total = 1
    
#     # x를 y번 곱해 준다
#     for i in range(y):
#         total *= x
    
#     return total
# 이 알고리즘의 시간 복잡도는 O(y)O(y)인데요. O(\lg{y})O(lgy)로 더 빠르게 할 수는 없을까요?

# 주의


def power(x, y):
    # 코드를 작성하세요.
    if y == 0:
        return None
    
    return power(x, y-1)
        
        

# 테스트
print(power(3, 5))
print(power(5, 6))
print(power(7, 9))









#재귀 시도
# def power(x, y):
#     # 코드를 작성하세요.
#     if y == 0:
#         return None
    
#     return power(x, y-1)
        


# ###합병 정렬 시도

# def power(x, y):
#     # 코드를 작성하세요.
#     if y == 0:
#         return 1
#     if y == 1:
#         return x
        
#     if y == 2:
#         return x*x
        
#     return power(x, y//2) * power(x, y//2 + 1)
        


# def power(x, y):
#     # 코드를 작성하세요.
#     if y == 0:
#         return 1
        
#     if y > 0:
#         return x * power(x, y-1)
        
#     return power(x, y//2) * power(x, y//2)
        