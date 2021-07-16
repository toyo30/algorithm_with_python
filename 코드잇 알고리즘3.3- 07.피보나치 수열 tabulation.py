# 실습과제 다이나믹 프로그래밍
# n번째 피보나치 수를 찾아주는 함수 fib_tab을 작성해 보세요.

# fib_memo는 꼭 tabulation 방식으로 구현하셔야 합니다!

# 기본 코드

#def fib_tab(n):
    # 코드를 작성하세요.














# def fib_tab(n):
#     # 코드를 작성하세요.
#     fib_dic = {}
    
#     for i in range(1, n+1):
#         if i == 1 or i == 2:
#             fib_dic[i] = 1
        
#         else:
#             fib_value = fib_dic[i-1] + fib_dic[i-2]
#             fib_dic[i] = fib_value
    
#     return fib_dic[n]



def fib_tab(n):
    # 코드를 작성하세요.
    fib_list = []
    
    for i in range(0, n+1):

        if i == 0:
            fib_list.append(0)
        elif i == 1 or i == 2:
            fib_list.append(1)
        else:
            fib_value = fib_list[i-1] + fib_list[i-2]
            fib_list.append(fib_value)
    
    return fib_list[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))






# BEST 답변
# 우선 리스트와 사전에 대해 간단히 설명을 드리자면:

# 리스트 - 오브젝트를 순서대로 저장하는 자료구조이고 (e.g. ['Alice', 'Bob']) 데이터 접근은 인덱스로 합니다 (O(1) 연산입니다).

# 사전 - key-value pair들을 저장하는 자료구조이고 (e.g. {'Alice':'01012345678', 'Bob':'01087654321'}) 데이터 접근은 key로 합니다 (O(1) 연산입니다).

# 따라서 쓰이는 용도가 약간 다릅니다. 만약 전화번호부를 구현하려면 위와 같이 사전으로는 쉽지만 리스트로는 어렵습니다. 쓰이는 용도가 다르기 때문에 두 자료구조를 비교하기는 어렵지만 장점을 몇가지 알려드린다면:

# 리스트 - 리스트 끝에 데이터를 append하는것이 빠르고 인덱스로 데이터 접근도 빠릅니다. 사전에 비해 메모리를 덜 차지합니다.

# 사전 - 탐색 (lookup)이 빠릅니다: 리스트에 'Alice'가 있는지 확인하는것은 O(n) 이지만 사전에 'Alice'가 있는지 확인하는것은 O(1)입니다.

# 마지막으로 피보나치 수열 문제의 경우 리스트, 사전 둘 다 적합하다고 생각합니다 (굳이 따지자면 리스트가 메모리를 덜 차지할 것 같네요).









