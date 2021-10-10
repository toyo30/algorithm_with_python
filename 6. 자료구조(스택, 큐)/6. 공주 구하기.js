// 스택으로 풀려고 했음. 스택으로도 풀 수 있긴 함. 
function solution(N, K) {
    var answer = 0;
    let stack = [];

    let num = [];
    for(let i = 1; i <= N; i++){
        num.push(i);
    }

    while(true){
        for(let x = 0; x < num.length; x++){
            stack.push(num[x])

            if(num.length === 2){
                stack.push(num[x])
            }

            if(stack.length === K) {

                stack = [];
                stack.push(num[x + 1])
                num.splice(num.indexOf(num[x]), 1)
            }
        }

        if(num.length === 1) {
            answer = num[0];
            break;  
        }           
    }
    return answer;
}
    
console.log(solution(8, 3));