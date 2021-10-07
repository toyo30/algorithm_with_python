function solution(str) {
    var answer = 0;
    var stack = [];
    for(let x of str){
        if(x === '(') stack.push()

        else if(x === ')') stack.pop()
    
    }
    
    answer += 1;
    
    return answer;
}
    
    
let str = '()(((()())(())()))(())';

console.log(solution(str));