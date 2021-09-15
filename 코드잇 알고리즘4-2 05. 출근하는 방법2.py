# 알고리즘 연습 Level 2
# 05. 출근하는 방법 2



#실습과제
# 영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라갑니다. 결국 계단을 오를 수 있는 모든 방법으로 계단을 올라갔는데요.

# 이제 다르게 계단을 올라갈 수는 없을까 고민하던 영훈이는 특이한 방법으로 계단을 오르려고 합니다.

# 가령 계단을 한 번에 1, 2, 4 칸씩 올라가 보는 건데요. 예를 들어서 계단을 4개를 올라가야 되면:

# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# 4
# 총 5개 방법이 있네요.

# 함수 staircase는 파라미터로 총 계단 수 n 그리고 한 번에 올라갈 수 있는 계단 수를 possible_possible_steps로 받고, 올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴합니다.

# 그러니까 n이 3, possible_possible_steps 가 [1, 2, 3]이면, 계단 총 3칸을 1, 2, 3칸씩 갈 수 있을 때 오르는 방법의 수를 수하는 거죠. 단, possible_possible_steps에는 항상 1이 포함된다고 가정합니다.





# 높이 n개의 계단을 올라가는 방법을 리턴한다
# def staircase(stairs, possible_steps):
#     # 코드를 쓰세요
#     list_stairs = [0, 1]
    
#     for i in range(1, stairs + 1):
#         if i < possible_steps[0]:
#             return None # 첫 번째 스탭보다 작으면 계단을 오를 수 없다. 
#         elif i < possible_steps[1]:
#             list_stairs.append(staircase((stairs - possible_steps[0]), possible_steps[:1]))
#             return list_stairs[i]
#         elif i < possible_steps[2]:
#             list_stairs.append(staircase((stairs - possible_steps[0]), possible_steps[:2]) + staircase((stairs - possible_steps[1]), possible_steps[:2]))
#             return list_stairs[i]
#         else:
#             list_stairs.append(staircase((stairs - possible_steps[0]), possible_steps) + staircase((stairs - possible_steps[1]), possible_steps) + staircase((stairs - possible_steps[2]), possible_steps))
    
#     return list_stairs[stairs]
# print(staircase(5, [1, 2, 3]))
# print(staircase(6, [1, 2, 3]))
# print(staircase(7, [1, 2, 4]))
# print(staircase(8, [1, 3, 5]))


def staircase(stairs, possible_steps):
    # 코드를 쓰세요
    list_stairs = [0]

    for i in range(possible_steps[0], stairs + 1):
        if i < possible_steps[1]:
            step_value = 1
            list_stairs.append(step_value)
        elif i == possible_steps[1]:
            step_value = 2
            list_stairs.append(step_value)
        elif i < possible_steps[2]:
            step_value = list_stairs[i - possible_steps[0]] +  list_stairs[i - possible_steps[1]]
            list_stairs.append(step_value)
        elif i == possible_steps[2]:
            step_value = list_stairs[i - possible_steps[0]] +  list_stairs[i - possible_steps[1]] + 1
            list_stairs.append(step_value)
        else:
            step_value = list_stairs[i - possible_steps[0]] +  list_stairs[i - possible_steps[1]] + list_stairs[i - possible_steps[2]]
            list_stairs.append(step_value)
    return list_stairs[stairs]


print(staircase(5, [1, 2, 3]))
print(staircase(6, [1, 2, 3]))
print(staircase(7, [1, 2, 4]))
print(staircase(8, [1, 3, 5]))