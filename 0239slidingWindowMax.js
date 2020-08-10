/*
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。
你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？
 
示例:

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7] 
解释: 

  滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

 // this problem requires us to use deque 
var maxSlidingWindow = function(nums, k) {
    // declare two empty array
    // window is used to store index while res is used to store result
    let res = [];
    let window = [];
    const len = nums.length;
    // consider special situation
    if(nums.length === 0 || k <= 0) return res;
    // iterate the array
    for(let i = 0; i < len; i++){
        // if current index minus the first index of the window larger than k
        if(i - window[0] >= k){
            // then remove the first element(means move the window to ensure it contains k elements)
            window.shift();
        }
        // pop out all the elements in the window which are smaller than the new data 
        // this can make sure that the first data is the largest one
        while(nums[window[window.length - 1]] <= nums[i]){
            window.pop();
        }
        // push new data's index to the window
        window.push(i);
        // if current index is larger than k - 1 which can ensure each three data produces a reuslt 
        if(i >= k - 1){
            // add the first data in the window to the result array
            res.push(nums[window[0]]);
        }
    }
    return res;
}