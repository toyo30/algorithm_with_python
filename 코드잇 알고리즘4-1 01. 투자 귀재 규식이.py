# Lesson_typepassed_checker
# 알고리즘 연습 Level 1
# 01. 투자 귀재 규식이 I

# 11
# profile_photo

# 알고리즘의 정석
# 토픽 4
# 문제 해결 능력 기르기
# 0/12 완료

# 알고리즘 연습 Level 1
# 알고리즘 연습 Level 2
# 알고리즘 연습 Level 3
# 01. 중복되는 항목 찾기 II
# 02. 리스트 항목 합 탐색
# 03. 강남역 폭우 II
# 실습과제
# 규식이는 친구들 사이에서 투자의 귀재로 알려져 있습니다. 페이수북과 인수타그램에 자신의 성과를 과시하기 때문인데요. 사실 규식이가 그 정도의 실력자는 아닙니다. 성과가 좋을 때에만 SNS에 공유해서 그렇게 비춰질 뿐이죠.

# 계속해서 멋진 모습을 보여주기 위해, 특정 기간 중 수익이 가장 큰 구간을 찾아내는 함수 sublist_max를 작성해 보려고 합니다.

# Brute Force 방법을 이용해서 이 문제를 한 번 풀어봅시다!

# 함수 설명
# 우선 함수 sublist_max는 파라미터로 리스트 profits를 받는데요. profits에는 며칠 동안의 수익이 담겨 있습니다. 예를 들어서 profits가 [7, -3, 4, -8]이라면 첫 날에는 7달러를 벌었고, 둘째 날에는 3달러를 잃었고, 셋째 날에는 4달러를 벌었고, 마지막 날에는 8달러를 잃은 거죠.

# sublist_max 함수는 profits에서 최대 수익을 내는 구간의 수익을 리턴합니다.

# profits가 [7, -3, 4, -8]이라면 무엇을 리턴해야 할까요? profits에서 가장 많은 수익을 낸 구간은 [7, -3, 4]입니다. 이 구간에서 낸 수익은 8달러이니, 8을 리턴하면 되겠죠!

# 만약 profits가 [-2, -3, 4, -1, -2, 1, 5, -3]이라면? profits에서 수익이 가장 큰 구간은 [4, -1, -2, 1, 5]입니다. 이 구간에서 낸 수익은 7달러이니, 7을 리턴하겠죠?

def sublist_max(profits):
    # 코드를 작성하세요. 
    max_value = 0
    for i in range(len(profits)):
        sum_value = 0
        for j in range(len(profits[i:])):
            sum_value += profits[i:][j]
            max_value = max(sum_value, max_value)
    
    return max_value
        

# 테스트
print(sublist_max([4, 3, 8, -2, -5, -3, -5, -3]))
print(sublist_max([2, 3, 1, -1, -2, 5, -1, -1]))
print(sublist_max([7, -3, 14, -8, -5, 6, 8, -5, -4, 10, -1, 8]))
