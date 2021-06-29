def binary_search(element, some_list):
    start_index = 0
    end_index = len(some_list) - 1
    
    while start_index <= end_index:
        midpoint = (start_index + end_index) // 2
        if some_list[midpoint] == element:
            return midpoint
        elif some_list[midpoint] > element:
            end_index = midpoint - 1
        else:
            start_index = midpoint + 1
    return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))

#이해해보기
# def binary_search(element, some_list):
#     midpoint = len(some_list)//2 
#     a = 0
#     end =10
#     while a < end:
#         if some_list[midpoint] == element:
#             return midpoint
#         elif some_list[midpoint] < element:
#             midpoint = (len(some_list) + midpoint)//2
#         else :
#             midpoint = (0 + midpoint)//2
#     return None


# def binary_search(element, some_list):
#     a = len(some_list)//2    
#     for i in range(len(some_list)):
#         if some_list[a] == element:
#             return a
#         elif some_list[a] < element:
#             a = (len(some_list) + a)//2
#         else :
#             a = (0 + a)//2
#     return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
# def variable_num(apple):
#     if 2**i>len(apple):
#         for 
        
#         a = len(apple)//2
    
#         if True:
#             a +=100
#         print(a)
#         return a

   

# print(variable_num("alskdjfla"))

