# 두 요소의 위치를 바꿔주는 helper function

def swap_elements(my_list, index1, index2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
    
# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    p = end
    i = start
    b = start

    
    while i <p:
        if my_list[i] <= my_list[p]:
            swap_elements(my_list, b, i)
            b +=1
        i += 1
        
    swap_elements(my_list,b,p)

    p = b

    return p
        
# 퀵 정렬
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    if end-start < 1:
        return
    
    a = partition(my_list, start, end)

    partition(my_list, start, a-1)
    partition(my_list, a+1, end)

    

    
        

    
    
list0 = [5, 2, 3]
print(quicksort(list0, 0, len(list0) - 1), "list0 =print quicksort")
quicksort(list0, 0, len(list0) - 1)
print(list0, "----")
    
   
list1 = [5, 2, 4, 6, 7]
print(quicksort(list1, 0, len(list1) - 1), "list1 =print quicksort")
quicksort(list1, 0, len(list1) - 1)
print(list1, "----")


list2 = [5, 2, 4, 6, 3]
print(quicksort(list2, 0, len(list2) - 1), "list2 = print quicksort")
quicksort(list2, 0, len(list2) - 1)
print(list2, "---")


list3 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list3, 0, len(list3) - 1)
print(list3)

# 테스트 2
list4 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list4, 0, len(list4) - 1)
print(list4)

# 테스트 3
list5 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list5, 0, len(list5) - 1)
print(list5)

    

 



    # if len(my_list) ==4:
    #     pivot_index = partition(my_list, start, end)
    #     my_list = my_list = quicksort(my_list[:pivot_index], start, pivot_index-1) + [my_list[pivot_index]] + quicksort(my_list[pivot_index+1:], pivot_index+1, end)
    #     return my_list
        

        
  

        # my_list = quicksort(my_list[:pivot_index], start, pivot_index-1) + [my_list[pivot_index]] + quicksort(my_list[pivot_index+1:], pivot_index+1, end)
        # return my_list

        
# 테스트 1xs

