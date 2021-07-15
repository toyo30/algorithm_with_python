# 실습과제 다이나믹 프로그래밍
# n번째 피보나치 수를 찾아주는 함수 fib_memo을 작성해 보세요.

# fib_memo는 꼭 memoization 방식으로 구현하셔야 합니다!

# 기본 코드


def fib_memo(n, cache):
    return
def fib(n):
    fib_cache = {}
    return fib_memo(n, fib_cache)







# 테스트
print(fib(10))
print(fib(50))
print(fib(100))









# 답안
# 다이나믹 프로그래밍
def fib_memo(n, cache):
    # 코드를 작성하세요.
    #n 번재 피보나치 수열을 정하기
    if n < 3:
        return 1
    
    # 수를 계산한 경우
    if n in cache:
        return cache[n]

    # 수를 계산하지 않은 경우
    fib_value = fib(n - 1) + fib(n -2)
    cache[n] = fib_value
    return cache[n]


def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    
    #피보나치 수열을 만드는 방법은? 
    #빼주어서, 딕셔너리에 더해주기, -->  딕셔너리에 저장하는 방법은?
    return fib_memo(n, fib_cache)



# 재귀함수를 사용하지 않은 경우 
def fib_memo(n, cache):
    
    return cache[n]

def fib(n):
    
    fib_cache = {}
    
    for i in range(1, n + 1):
        if i == 1 or i ==2:
            fib_cache[i] = 1
        else:
            fib_value = fib_cache[i - 1] + fib_cache[i - 2]
            fib_cache[i] = fib_value
            
    return fib_memo(n, fib_cache)


