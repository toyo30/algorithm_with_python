function solution(price, money, count) {
    var answer = -1;
    var value = 0;
    for (var i = 1; i < count + 1; i++){
        value += price * i
    };
    if (value <= money){
        return 0;
    };
    var answer = value - money;
    return answer;
}

console.log(solution(3, 20, 4));