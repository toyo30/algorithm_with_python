function solution(a, b, c, d, e, f, g){
    let answer;
    let arr_Box = [a, b, c, d, e, f, g];

    answer = Math.min.apply(null, arr_Box);


    return answer
}

console.log(solution(5, 3, 7, 11, 2, 15, 17));



//Math.min만 써도 됨. 

//배열을 쓸때는 Math.min(...arr);   arr[0], arr[1], arr[2], arr[3] ... 이렇게 전게됨. 

//Math.min.apply(null, arr); 첫번재 인자는 this에다가 컨트롤할 수 있는 객체를 사용할 수 있음. 