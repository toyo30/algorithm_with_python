# Greedy Algorithm
# 10. 수강 신청


# 실습과제
# 100XP
# 이번 학기 코드잇 대학교의 수업 리스트가 나왔습니다.

# [(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 6), (13, 16), (9, 11), (1, 8)]
# 리스트에 담겨있는 튜플들은 각각 하나의 수업을 나타냅니다. 각 튜플의 0번째 항목은 해당 수업의 시작 교시, 그리고 1 번 항목은 해당 수업이 끝나는 교시입니다. 예를 들어서 0번 인덱스에 있는 튜플값은 (4, 7)이니까, 해당 수업은 4교시에 시작해서 7교시에 끝나는 거죠.

# (2, 5)를 듣는다고 가정합시다. (4, 7) 수업은 (2, 5)가 끝나기 전에 시작하기 때문에, 두 수업은 같이 들을 수 없습니다. 반면, 수업 (1, 3)과 (4, 7)은 시간이 겹치지 않기 때문에 동시에 들을 수 있습니다.

# (단, (2, 5), (5, 7)과 같이 5교시에 끝나는 수업과 5교시에 시작하는 수업은 서로 같이 듣지 못한다고 가정합니다)

# 열정이 불타오르는 신입생 지웅이는 최대한 많은 수업을 들을 수 있는 수업 조합을 찾아주는 함수 course_selection 함수를 작성하려고 합니다.

# course_selection은 파라미터로 전체 수업 리스트를 받고 가능한 많은 수업을 담은 리스트를 리턴합니다.

def course_selection(course_list):
    # 코드를 작성하세요.
    course_schedule = []
    sot_list = sorted(course_list)
    course_schedule.append(sot_list[0])

    for i in range(1, len(course_list)):
        if sot_list[i][1] > course_schedule[-1][1] and sot_list[i][0] > course_schedule[-1][0] and sot_list[i][0] > course_schedule[-1][1]:
            course_schedule.append(sot_list[i])
        elif sot_list[i][1] < course_schedule[-1][1]:
            course_schedule.pop()
            course_schedule.append(sot_list[i])
    return course_schedule

    

# 테스트
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 6), (13, 16), (9, 11), (1, 8)]))
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))



#람다를 사용해서 원하는 방식으로 정렬할 수 있음. 그렇다면 함수가 어떻게 더 간단해질 수 있을까?


# a = [(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]


# sort_a = sorted(a, key = lambda x: x[1])


# print(sort_a)  이걸 가지고 구현해보기




