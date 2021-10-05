
    function solution(str){
        let answer = "YES";
        let stack = [];
        for(let x of str){
            if(x === '(') stack.push(x);
            else {
                if(stack.length === 0) return "No"
                stack.pop()
            };
        };
    
        if(stack.length === 0) return answer;
        else return "NO"
    
    
    
    }
    
    
    
    let s = "()()()()()()()())";
    console.log(solution(s));