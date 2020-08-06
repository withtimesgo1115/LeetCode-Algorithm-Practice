/*
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.

*/

var findMaxConsecutiveOnes = function(nums) {
    let c = 0, l = 0;
    if(nums.indexOf(0) !== -1){
        for(let i = 0; i < nums.length; i++){
            if(nums[i] === 1){
                c++;
                if(c > l){
                    l = c;
                }
            }
            else{
                c = 0;
            }
        }
        return l;
    }
    else{
        return nums.length;
    }
};