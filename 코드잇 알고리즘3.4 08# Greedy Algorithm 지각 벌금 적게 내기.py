# Greedy Algorithm
# 08. 지각 벌금 적게 내기

# 실습과제
# 익중이네 밴드부는 매주 수요일 오후 6시에 합주를 하는데요. 멤버들이 너무 상습적으로 늦어서, 1분에 1달러씩 내야 하는 벌금 제도를 도입했습니다.

# 그런데 마침 익중이와 친구 넷이 놀다가 또 지각할 위기입니다. 아직 악보도 출력해 놓지 않은 상황이죠.

# 어차피 같이 놀다 늦은 것이니 벌금을 다섯 명이서 똑같이 나눠 내기로 하고, 벌금을 가능한 적게 내는 방법을 고민해 보기로 합니다.

# 다섯 사람이 각각 출력해야 하는 페이지 수는 3장, 1장, 4장, 3장, 2장입니다. 프린터는 한 대밖에 없고, 1장을 출력하기 위해서는 1분이 걸립니다.

# 현재 순서대로 출력한다면,

# 첫 번째 사람: 33분 지각
# 두 번째 사람: 3 + 13+1분 지각
# 세 번째 사람: 3 + 1 + 43+1+4분 지각
# 네 번째 사람: 3 + 1 + 4 + 33+1+4+3분 지각
# 다섯 번째 사람: 3 + 1 + 4 + 3 + 23+1+4+3+2분 지각
# 총 39달러의 벌금을 내야 합니다.

# 흠… 더 적게 내는 방법이 있지 않을까요?

# 출력할 페이지 수가 담긴 리스트 pages_to_print를 파라미터로 받고 최소 벌금을 리턴해 주는 함수 min_fee를 Greedy Algorithm으로 구현하세요.


def min_fee(pages_to_print):
    # 코드를 작성하세요.
    min_value = 0
    number = len(pages_to_print)
    for i in sorted(pages_to_print):
        min_value += i*number
        number -= 1
    return min_value
        


# 테스트
print(min_fee([6, 11, 4, 1]))
print(min_fee([3, 2, 1]))
print(min_fee([3, 1, 4, 3, 2]))
print(min_fee([8, 4, 2, 3, 9, 23, 6, 8]))


# def min_fee(pages_to_print):
#     # 인풋으로 받은 리스트를 정렬시켜 준다
#     sorted_list = sorted(pages_to_print)

#     # 총 벌금을 담을 변수
#     total_fee = 0

#     # 정렬된 리스트에서 총 벌금 계산
#     for i in range(len(sorted_list)): #공간 복잡도 줄이기, 어차피 인댁스번호와, 인원수가 같으니까.
#         total_fee += sorted_list[i] * (len(sorted_list) - i)

#     return total_fee


# 결국 생각하면 다 풀리는 구나!


