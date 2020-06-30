const lengthOfLIS = function(nums){
    // store array's length
    const len = nums.length;
    // handle border condition
    if(!len){
        return 0;
    }
    // init state values in an array with 1
    const dp = (new Array(len)).fill(1);
    // init maxLen
    let maxLen = 1;
    // iterate the whole array from second position
    for(let i = 1; i < len; ++i){
        // relook if we check current data
        for(let j = 0; j < i; ++j){
            // if meet a smaller data, it means there is a subarray which can meet the goal
            if(nums[j] < nums[i]){
                // update current state
                dp[i] = Math.max(dp[i], dp[j]+1);
            }
        }
        // update current maxLen
        if(dp[i] > maxLen){
            maxLen = dp[i];
        }

        // return result
        return maxLen;
    };
}