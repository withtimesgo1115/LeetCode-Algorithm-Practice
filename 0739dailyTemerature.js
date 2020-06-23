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