# Lesson_typepassed_checker
# 재귀 함수 연습
# 06. 하노이의 탑

# 1
# profile_photo

# 알고리즘의 정석
# 토픽 2
# 재귀 함수
# 8/9 완료

# 재귀 함수
# 재귀 함수 연습
# 01. 피보나치 수열
# 02. 숫자 합
# 03. 자릿수 합
# 04. 리스트 뒤집기
# 05. 이진 탐색 재귀로 구현해보기
# 06. 하노이의 탑
# 실습과제
# 100XP
# 하노이의 탑
# 하노이의 탑 게임 아시나요? 이 게임의 목표는 왼쪽 기둥에 있는 원판들을 모두 오른쪽 기둥으로 옮기는 것입니다. 지켜야할 규칙은 두가지입니다:

# 한 번에 하나의 원판만 옮길 수 있다.
# 큰 원판이 작은 원판 위에 있어서는 안 된다.


# (출저: 위키피디아)

# 과제
# 하노이의 탑 게임의 해답을 출력해주는 함수 hanoi를 쓰세요. hanoi는 파라미터로 원판 수 num_disks, 게임을 시작하는 기둥 번호 start_peg, 그리고 목표로 하는 기둥 번호 end_peg를 받고, 재귀적으로 문제를 풀어 원판을 옮기는 순서를 모두 출력합니다.

# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# def hanoi(num_disks, start_peg, end_peg):
#     # 코드를 입력하세요.

# # 테스트 코드 (포함하여 제출해주세요)
# hanoi(3, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 가장 작은 원판의 번호는 1번이고 가장 큰 원판의 번호는 num_disks번입니다. 그리고 왼쪽 기둥이 1번, 가운데 기둥이 2번, 오른쪽 기둥이 3번입니다.

# 원판 하나인 경우
# hanoi(1, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 원판 두개인 경우
# hanoi(2, 1, 3)
# 1번 원판을 1번 기둥에서 2번 기둥으로 이동
# 2번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 3번 기둥으로 이동
# 원판 세개인 경우
# hanoi(3, 1, 3)
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 2번 원판을 1번 기둥에서 2번 기둥으로 이동
# 1번 원판을 3번 기둥에서 2번 기둥으로 이동
# 3번 원판을 1번 기둥에서 3번 기둥으로 이동
# 1번 원판을 2번 기둥에서 1번 기둥으로 이동
# 2번 원판을 2번 기둥에서 3번 기둥으로 이동
# 1번 원판을 1번 기둥에서 3번 기둥으로 이동
# 힌트를 최대한 보지 않고, 스스로의 힘으로 푸시는 것이 좋습니다. 만약 도저히 모르겠다면, 최소한의 힌트만 참고해주세요!


def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    # 코드를 입력하세요.
    if num_disks == 1:
        return move_disk(num_disks, start_peg, end_peg)
    
    if num_disks > 1:
        return hanoi(num_disks-1, start_peg, end_peg-1), move_disk(num_disks, start_peg, end_peg), hanoi(num_disks-1, end_peg-1, end_peg)

# 테스트 코드 (포함하여 제출해주세요)
hanoi(2, 1, 3)
print("-----------------")
hanoi(3, 1, 3)




# def move_disk(disk_num, start_peg, end_peg):
#     print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))

# def hanoi(num_disks, start_peg, end_peg):
#     # 코드를 입력하세요.
#     if num_disks == 1:
#         return move_disk(num_disks, start_peg, end_peg)
    
#     if num_disks==2 and start_peg == 1 and end_peg=2:
#         return move_disk(1, 1, 3)
#         return move_disk(2, 1, 2)
#         return move_disk(1, 3, 2)
#     elif num_disks==2 and start_peg == 1 and end_peg = 3:
#         return move_disk(1, 1, 2)
#         return move_disk(2, 1, 3)
#         return move_disk(1, 2, 3)
#     elif num_disks==2 and start_peg == 2 and end_peg = 1:
#         return move_disk(1, 2, 3)
#         return move_disk(2, 2, 1)
#         return move_disk(1, 3, 1)
#     else num_disks==2 and start_peg == 2 and end_peg = 3:
#         return move_disk(1, 2, 1)
#         return move_disk(2, 2, 3)
#         return move_disk(1, 1, 3)
#     return hanoi(num_disks-1, start_peg, end_peg-1)
#     return move_disk(num_disks, start_peg, end_peg)
#     return hanoi(num_disks-1, end_peg-1, end_peg)
    
# # 테스트 코드 (포함하여 제출해주세요)
# hanoi(3, 1, 3)