function solution(N, K) {
    var answer = 0;
    let stack = [];

    let num = [];
    for(let i = 1; i <= N; i++){
        num.push(i)
    }

    while(true){
        if(num.length === 1) {
            answer = num[0];
            break;  
        }

        for(let x of num){
            stack.push(x)
            
            if(stack.length === K) {
                
                let a = stack.pop()
                num.splice(num.indexOf(a), 1)
                continue;
            }
        }           
    }
    return answer;
}
    
console.log(solution(8, 3));