# Brute Force
# 06. 강남역 폭우

# profile_photo

# 알고리즘의 정석
# 토픽 3
# 알고리즘 패러다임
# 42/43 완료

# Brute Force
# 01. 알고리즘 패러다임
# 02. Brute Force 소개
# 03. 카드 뭉치 최대 조합
# 04. Brute Force 평가
# 05. 가까운 매장 찾기
# 06. 강남역 폭우
# Divide and Conquer
# Dynamic Programming
# Greedy Algorithm
# 실습과제
# 95XP
# 강남역에 엄청난 폭우가 쏟아진다고 가정합시다. 정말 재난 영화에서나 나올 법한 양의 비가 내려서, 고층 건물이 비에 잠길 정도입니다.

# 그렇게 되었을 때, 건물과 건물 사이에 얼마큼의 빗물이 담길 수 있는지 알고 싶은데요. 그것을 계산해 주는 함수 trapping_rain을 작성해 보려고 합니다.

# 함수 trapping_rain은 건물 높이 정보를 보관하는 리스트 buildings를 파라미터로 받고, 담기는 빗물의 총량을 리턴해 줍니다.

# 예를 들어서 파라미터 buildings로 [3, 0, 0, 2, 0, 4]가 들어왔다고 합시다. 그러면 0번 인덱스에 높이 33의 건물이, 3번 인덱스에 높이 22의 건물이, 5번 인덱스에 높이 44의 건물이 있다는 뜻입니다. 1번, 2번, 4번 인덱스에는 건물이 없습니다.

# 그러면 아래의 사진에 따라 총 1010 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 10을 리턴하는 거죠.



# 이번에는 파라미터 buildings로 [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]가 들어왔다고 합시다. 그러면 아래의 사진에 따라 총 66 만큼의 빗물이 담길 수 있습니다. 따라서 trapping_rain 함수는 6을 리턴하는 거죠



# 이 정보를 기반으로, trapping_rain 함수를 작성해 보세요!

# 예시
# # 테스트
# print(trapping_rain([3, 0, 0, 2, 0, 4]))
# print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 10
# 6


def trapping_rain(buildings):
    rain_sum = 0
    standard_value = int(buildings[0])
    for i in range(1, len(buildings) - 1):
        max_value = max(buildings[i + 1:])
        rain_sum += min(max_value, standard_value) - buildings[i]
        standard_value = max(buildings[:i+1])
    return rain_sum


    # 코드를 작성하세요
    # rain_sum = 0
    # standard_index = 0
    # standard_value = buildings[standard_index]

    # for i in range(1, len(buildings)):
    #     if buildings[i] > standard_value:
    #         rain_sum += (i-standard_index-1) * standard_value
    #         if standard_value >= 1:
    #             for j in range(standard_index + 1, i):
    #                 rain_sum -= buildings[j]
    #                 standard_index = i + 1
    # return rain_sum

# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))


# def trapping_rain(buildings):
#     # 코드를 작성하세요
#     rain_amount = 0
#     building_height = buildings[0]
#     standard_building =[]
#     for i in buildings:
#         if i > 0 and i > building_height:
#             i = building_height
#             max
#         while 
#         for 
#         if 
            
#          rain_amount += 
    
#     return rain_amount

# # 테스트
# print(trapping_rain([3, 0, 0, 2, 0, 4]))
# print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))