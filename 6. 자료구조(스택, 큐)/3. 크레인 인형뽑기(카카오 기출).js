// function solution(board, moves){
//     var answer = 0;
//     var stack = [];
//     for(let x of moves) {
//         for(let i in board){
//             if(board[i][x-1] !== 0) {
//                 if(stack[-1] === board[i][x-1]) {
//                     stack.pop();
//                     answer += 2;
//                 }
//             stack.push(board[i][x-1]);
//             board[i][x-1] = 0;
            
//             }
            
//         }
//     }
//     //사라진 인형의 개수를 return 
//     return answer;
// };
    

function solution(board, moves) {
    var answer = 0;
    var stack = [];
    for(let x of moves) {
        for(let i in board){
            if(board[i][x-1] !== 0) {
                let number = board[i][x-1];
                board[i][x-1] = 0;
                if(stack[stack.length - 1] === number) {
                    stack.pop()
                    answer += 2;
                }
                else stack.push(number);
                break;
    
            };
        }
    }
    return answer;
}
    
    
let board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]];
let moves = [1,5,3,5,1,2,1,4];
console.log(solution(board, moves));