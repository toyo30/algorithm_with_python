function solution(str) {
    var answer = 0;
    let stack = [];
    for(let x = 0; x < str.length; x++){
        if(str[x] === '('){
            stack.push(str[x])
        }
        else if(str[x] ===')'){
            stack.pop()
            if(str[x-1] ==='(') {
                answer += stack.length
            }
            else answer += 1;
        }
    }
    return answer;
}

let str = '()(((()())(())()))(())';

console.log(solution(str));