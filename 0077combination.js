var combine = function(n, k) {
    // init result array and combination array
    const res = [];
    const subset = [];
    // enter dfs from number 1
    dfs(1);

    // define dfs function, input is current index(number)
    function dfs(index){
        // border condition
        // if subset's len is equal to k then push to res and return
        if(subset.length === k){
            res.push(subset.slice());
            return;
        }
        // iterate from current number to n (index - n)
        for(let i = index; i <= n; ++i){
            // current number exists in the combination
            subset.push(i);
            // run dfs further based on current num exists
            dfs(i+1);
            // current number doesn't exist in the combination, pop out from the stack
            subset.pop();
        }
    }
    return res;
};