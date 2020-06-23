const maxSlidingWindow = function(nums, k) {
    // store the length
    const len = nums.length;
    // init an output array
    const res = [];
    // define left pointer and right pointer (index)
    let left = 0;
    let right = k - 1;
    // use while loop
    while(right < len){
        // get the max value in the interval
        const max = calcMax(nums, left, right);
        // add the value and move the pointers
        res.push(max);
        left++;
        right++;
    }
    // return the output array
    return res;
};

//define a function to find the max value in the interval
const calcMax = function(arr, left, right){
    // if arr is empty array
    if(!arr || !arr.length){
        return;
    }
    // init a variable to store maximum value
    let maxNum = arr[left];
    // use for loop to iterate the interval
    for(let i = left; i <= right; i++){
        if(arr[i] > maxNum){
            maxNum = arr[i];
        }
    }
    return maxNum;
};