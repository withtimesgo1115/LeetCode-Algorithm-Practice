const permute = function(nums) {
    // store the length of the array
    const len = nums.length;
    // curr is used to record the current content
    const curr = [];
    // res is used to record the full permutes
    const res = [];
    // visited is used to avoid reusing a same number
    const visited = {};
    // define a dfs function whose input is the index of each position
    function dfs(nth){
        // if reach the impossible position(len+1) just return 
        if(nth === len){
            // the former positions have been occupied, then record curr's copy 
            res.push(curr.slice());
            return;
        }
        // check the numbers left now
        for(let i = 0; i < len; i++){
            // if nums[i] has not been used
            if(!visited[nums[i]]){
                // mark it 
                visited[nums[i]] = 1;
                // push nums[i] to the permute
                curr.push(nums[i]);
                // recursion here, call dfs again but use the next index
                dfs(nth+1);
                // nums[i] gives the position back
                curr.pop();
                // unmark it
                visited[nums[i]] = 0;
            }
        }
    }
    // use dfs from index 0
    dfs(0);
    return res;
};