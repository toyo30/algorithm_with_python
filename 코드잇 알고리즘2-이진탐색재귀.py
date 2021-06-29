def binary_search(element, some_list, start_index=0, end_index=None):
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    mid_index = (start_index + end_index)//2


    if element not in some_list:
        return None
    elif element == some_list[mid_index]:
        return mid_index
    elif element < some_list[mid_index]:
        some_list = some_list[0:mid_index]
        print(some_list)
        return binary_search(element, some_list)  
    else:
        some_list= some_list[mid_index + 1:]
        return binary_search(element, some_list)


print(binary_search(11, [0,1,2,3,4,5,6,7,8,9,10]))