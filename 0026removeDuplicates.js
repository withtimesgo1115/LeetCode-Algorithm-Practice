// use double pointers: one is the quick pointer the other is the slow pointer
// two pinters but it is not a nested iterations
// so it is O(n) in time and O(1) in space

// this function return the length of the new array
var removeDuplicates = function(nums){
    if(nums.length === 0) return 0;
    // the slow pointer 
    var i = 0;
    // the quick pointer
    for(let j = 1; j < nums.length; j++){
        // once it found two different elements, move forward the slow pointer
        // meanwhile assign current value of quick pointer to the slow pointer
        if(nums[i] !== nums[j]){
            i++;
            nums[i] = nums[j];
        }
        // for two same elements, just jump to the next one  
    }
    // finally return the slow pointer index + 1 
    return i + 1;
};