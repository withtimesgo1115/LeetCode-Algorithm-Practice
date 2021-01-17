/*
请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
*/

// Brute-force method
var dailyTemperatures = function(T) {
    let res = [];
    for(let i = 0; i < T.length; i++){
        let count = 0;
        let curT = T[i]; 
        let flag = false;
        for(let j = i + 1; j < T.length; j++){
           if(T[j] > curT){
               flag = true;
               count++;
               res.push(count);
               break;
           }
           else{
               count++;
           }
       } 
       if(!flag) res.push(0);
    }
    return res;
};


const dailyTemperatures = function(T){
    // store the length of the array
    const len = T.length;
    // init a stack to store index
    const stack = [];
    // init a result array and note that the array's length is fixed and we can fill with zero
    const res = (new Array(len)).fill(0);
    // iterate with for loop
    for(let i = 0; i < len; i++){
        // if the stack is not empty and meanwhile there is an increasing tendency
        while(stack.length && T[i] > T[stack[stack.length - 1]]){
            // pop corresponding index of the top position of the stack
            const top = stack.pop();
            // calculate difference of index between current data and the top of stack
            res[top] = i - top;
        }
        // if the stack is empty or there is no increaseing trend, just push current index to the stack
        stack.push(i);
    }
    return res;
};