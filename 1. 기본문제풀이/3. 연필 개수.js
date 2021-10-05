function solution(N){
    let answer = 0;
    while (N > 0) {N -= 12; answer++;};


    return answer
}

console.log(solution(25));




// function solution(N){
//     let answer = 0;
//     while (N > 0) N -= 12; answer++;;
        // 이렇게 하게 되면 반복문 바로 앞에 있는 코드까지를 포함하게 된다. 

// }
   