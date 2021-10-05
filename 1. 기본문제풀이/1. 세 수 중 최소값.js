
function solution1(a, b, c){
    let answer1 = 0;
    
    if  (a > b) answer1 = b;
    else answer1 = a;
    if (c < answer1)  answer1 = c;
    // 파이썬에서 pass 는 자바스크립트의 빈 블록

    return answer1;
};

console.log(solution1(3, 2, 7));



function solution1(a, b, c){
    let answer = 0;
    
    let arrBox = [ a, b, c];
    answer = Math.max.apply(null, arrBox);
    //answer = Math.max.apply(null, arrBox);

    return answer;
};

console.log(solution1(3, 2, 7));
  





console.log('asdfasfd')

console.log('asdjfjasdf')


console.log('12342351')