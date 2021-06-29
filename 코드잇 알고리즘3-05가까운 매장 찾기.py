# 제곱근 사용을 위한 sqrt 함수
from math import sqrt

# 두 매장의 직선 거리를 계산해 주는 함수
def distance(store1, store2):
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

def closest_pair(coordinates):
    min = []
    for i in test_coordinates:
        for j in test_coordinates:
            print(i, j, distance(i, j))

                

            
            
# 테스트
test_coordinates = [(2, 3), (12, 30), (40, 50)]

print(closest_pair(test_coordinates))