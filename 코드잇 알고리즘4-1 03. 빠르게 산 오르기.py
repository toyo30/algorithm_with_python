# 알고리즘 연습 Level 1
# 03. 빠르게 산 오르기

# profile_photo

# 알고리즘의 정석
# 토픽 4
# 문제 해결 능력 기르기
# 2/12 완료

# 알고리즘 연습 Level 1
# 01. 투자 귀재 규식이 I
# 02. 거듭 제곱 빠르게 계산하기
# 03. 빠르게 산 오르기
# 04. 중복되는 항목 찾기 I
# 알고리즘 연습 Level 2
# 알고리즘 연습 Level 3
# 실습과제
# 100XP
# 신입 사원 장그래는 마부장님을 따라 등산을 가게 되었습니다.

# 탈수를 방지하기 위해서 1km당 1L의 물을 반드시 마셔야 하는데요. 다행히 등산길 곳곳에는 물통을 채울 수 있는 약수터가 마련되어 있습니다. 다만 매번 줄서 기다려야 한다는 번거로움이 있기 때문에, 시간을 아끼기 위해서는 최대한 적은 약수터를 들르고 싶습니다.

# 함수 select_stops는 파라미터로 약수터 위치 리스트 water_stops와 물통 용량 capacity를 받고, 장그래가 들를 약수터 위치 리스트를 리턴합니다. 앞서 설명한 대로 약수터는 최대한 적게 들러야겠죠.

# 참고로 모든 위치는 km 단위이고 용량은 L 단위입니다. 그리고 등산하기 전에는 이미 물통이 가득 채워져 있으며, 약수터에 들르면 늘 물통을 가득 채운다고 가정합시다.

# 예시를 하나 볼게요.

# # 약수터 위치: [1km, 4km, 5km, 7km, 11km, 12km, 13km, 16km, 18km, 20km, 22km, 24km, 26km]
# # 물통 용량: 4L
# select_stops([1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26], 4)
# 처음에 4L의 물통이 채워져 있기 때문에, 장그래는 약수터에 들르지 않고 최대 4km 지점까지 올라갈 수 있습니다. 탈수 없이 계속 올라가기 위해서는 1km 지점이나 4km 지점에서 물통을 채워야겠죠?

# 최대한 적은 약수터를 들르면서 올라가야 하고, 마지막에 산 정상인 26km 지점의 약수터를 들르면 성공적인 등산입니다.

# 실행 결과
# [4, 7, 11, 13, 16, 20, 24, 26]
# [5, 8, 12, 17, 23, 28, 32, 38, 44, 47]

def select_stops(water_stops, capacity):
    
    stop_list = []

    for i in range(0, len(water_stops)):
        if water_stops[i] <= capacity:
            if capacity - water_stops[i] > 0:
                pass
            elif capacity - water_stops[i] ==0:
                stop_list.append(water_stops[i])
        elif water_stops[i] > capacity:
            if capacity - (water_stops[i] - stop_list[-1]) ==0:
                stop_list.append(water_stops[i])
            elif capacity - (water_stops[i] - stop_list[-1]) < 0:
                stop_list.append(water_stops[i - 1])
    stop_list.append(water_stops[-1])
    return stop_list

list1 = [1, 4, 5, 7, 11, 12, 13, 16, 18, 20, 22, 24, 26]
print(select_stops(list1, 4))

list2 = [5, 8, 12, 17, 20, 22, 23, 24, 28, 32, 38, 42, 44, 47]
print(select_stops(list2, 6))


#최적부분 구조와 ~~을 활용한 풀이.




# 내 답안 

# def select_stops(water_stops, capacity):
    
#     stop_list = []

#     for i in range(0, len(water_stops)):
#         if water_stops[i] <= capacity:
#             if capacity - water_stops[i] > 0:
#                 stop_list = [water_stops[i]]
#             elif capacity - water_stops[i] ==0:
#                 stop_list = [water_stops[i]]
    
#         elif water_stops[i] > capacity:
#             if capacity - (water_stops[i] - stop_list[-1]) ==0:
#                 stop_list.append(water_stops[i])
#             elif capacity - (water_stops[i] - stop_list[-1]) < 0:
#                 stop_list.append(water_stops[i - 1])
#     stop_list.append(water_stops[-1])
    
#     return stop_list