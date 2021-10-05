
    function solution(str){
        let answer ='';
        let stack = [];
        for(let x = 0; x < str.length; x++){
            if(str[x] === '('){
                stack.push(str[x]);

            } else if(str[x] ===')'){
                if(stack.length === 0) return "괄호가 올바르지 않습니다."
                stack.pop()
            } else {
                if(stack.length === 0) answer += str[x]
            };
        };
    
        return answer
    }
    
    
    
    let s = "(A(BC)D)EF(G(H)(IJ)K)LM(N)";
    console.log(solution(s));