/*
给定一个大小为 n 的数组，找到其中的多数元素。
多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2
*/

// method1 use map
var majorityElement = function(nums) {
    let mymap = new Map();
    const len = nums.length;
    let max = -Infinity;
    let res = 0;
    for(let i = 0; i < len; i++){
        if(mymap.get(nums[i]) === undefined){
            mymap.set(nums[i], 1);
        }
        else{
            mymap.set(nums[i], mymap.get(nums[i])+1);
        }
    }
    max = Math.max.apply(null,[...mymap.values()]);
    for(let [key, value] of mymap){
        if(value === max){
            res = key;
        }
    }
    return res;
};


// My own solution using map
var majorityElement = function(nums) {
    const map = new Map();
    let res = [];
    for(let i = 0; i < nums.length; i++){
        if(!map.has(nums[i])) map.set(nums[i], 1);
        else{
            let times = map.get(nums[i]);
            map.set(nums[i], times+1);
        }
    }
    for(let [key,val] of map){
        if(val > (nums.length / 2)) res.push(key); 
    }
    return res;
};

// method2 use sort
var majorityElement = function(nums) {
    nums.sort(function(a,b){
        return a - b;
    });
    const index = Math.floor(nums.length / 2);
    return nums[index];
};

