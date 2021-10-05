function solution(a, b, c){
    if (a + b > c && a + c > b && c + b > a){
        return "YES"
    }else {
        return "NO"
    }
}

console.log(solution(13, 33, 17));