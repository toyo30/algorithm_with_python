// 큐로 풀기
function solution(N, K) {
    var answer = 0;

    let num = [];
    for(let i = 1; i <= N; i++){
        num.push(i);
    }

    while(true){
        for(let x = 0; x < K; x++){
            num.push[num[x-1]]
            num.splice(x, 1)
        }

        if(num.length === 1){
            answer = num[0];
            break;
        }
    }
            
    return answer;
}
    
console.log(solution(7, 4));