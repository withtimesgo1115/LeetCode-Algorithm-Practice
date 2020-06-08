// my first violent method O(n*(n-1))
var twoSum = function(nums, target) {
    //var sortNums = nums.sort(); this will cause the array increases according to the character word
    var ans = []; 
    for(var i=0;i<nums.length;++i){
        for(var j=i+1;j<nums.length;++j){
            if(nums[i]+nums[j] === target){
                ans.push(i);
                ans.push(j);
                return ans;
            }
        }
    } 
    return ans;
};


// dalao's solution: O(n) in time / O(n) in space
// use a map to store the value and its index we had checked already
// use difference rather than addition to compare 
const twoSum = function (nums, target) {
    const map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const diff = target - nums[i];
        if (map.has(diff)) {
            return [map.get(diff), i];
        }
        map.set(nums[i], i);
    }
}