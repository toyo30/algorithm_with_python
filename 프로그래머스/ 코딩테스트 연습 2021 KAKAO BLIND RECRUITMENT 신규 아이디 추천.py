def solution(new_id):
    answer = ''

    # 1단계  
    new_id = new_id.lower()


    #2단계 
    character = '~!@#$%^&*()=+[{]}:?,<>/'
    for i in range(len(character)):
        new_id = new_id.replace(character[i], "")

    #3단계 
    
    if len(new_id) > 1:
        value = "{}".format(new_id[0])

    for i in range(1, len(new_id)):
        if new_id[i - 1] == "." and new_id[i] == ".":
            pass 
        else :
            value = "{}".format(value + new_id[i])
    
    new_id = value

    #4단계

    if new_id[0] == '.' and len(new_id) > 1:
        new_id = new_id[1:]
    elif new_id[-1] == '.' and len(new_id) > 1:
        new_id = new_id[:-1]
    elif len(new_id) == 1 and new_id[0] == '.':
        new_id = ''

        
    

    #5단계
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        new_id = new_id[0:15]
        if new_id[-1] == '.':
            new_id = new_id[0:14]
       
    
    #7단계
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id = new_id + new_id[-1] 
    

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution(""))




# 어떤 거는 출력되고, 어떤 거는 그냥 실행되고 끝. 