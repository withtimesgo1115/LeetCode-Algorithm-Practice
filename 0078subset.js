const subsets = function(nums){
    const res = [];
    const len = nums.length;
    const subset = [];
    
    // define dfs function which requires the index of number in nums
    function dfs(index){
        // just push since the content has been updated 
        res.push(subset.slice());
        // iterate from current number's index
        for(let i = index; i < len; ++i){
            // current number exists
            subset.push(nums[i]);
            // dfs further based on current number exists
            dfs(i+1);
            // current number doesn't exist
            subset.pop();
        }
    }

    dfs(0);

    return res;
}