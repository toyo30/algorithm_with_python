// let ttt = '()(((()()8)9(10())()))(())';
function solution(str) {
    var answer = 0;

    for(let x = 0; x < str.length; x++){
        let stack = [];
        let pointNum = 0;
        for(let t = x; t < str.length; t++){

            if(str[t] === '(') {
                stack.push(str[t]);
            } 
            else if(str[t] === ')'){
                stack.pop();
                if(stack.length === 0) {
                    if(str[t-1] === '(' || t == x) {
                        break;
                    }
                    answer += pointNum + 1;
                    break;
                    
                } 
                else {
                    if(str[t-1] === '('){
                        pointNum++;
                    }
                    
                }
            }

        }

    }
    
    
    return answer;
}
    
    
let str = '(((()(()()))(())()))(()())';

console.log(solution(str));