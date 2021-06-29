
# for i in range(5):
#     print(i, end='')

# #출력값 1234

# def function(a):
#     for i in range(5):
#         print(i, end='')


# print(function("A"))

#출력값 1234None


#함수는 리턴값이 없으면 None을 출력한다. 


def linear_search(element, some_list):
    for i in range(len(some_list)):
        if element == some_list[i]:
            return i
    return None#끝나면 None을 리턴하기. 

print(linear_search(2, [2, 3, 5, 7, 11]))
print(linear_search(0, [2, 3, 5, 7, 11]))
print(linear_search(5, [2, 3, 5, 7, 11]))
print(linear_search(3, [2, 3, 5, 7, 11]))
print(linear_search(11, [2, 3, 5, 7, 11]))