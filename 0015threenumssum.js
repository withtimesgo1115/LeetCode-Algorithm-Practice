/*
Once the pointer moved, there must be a comparision between new data and the old data
At the beginning, we also should check the current data and the former data in the iteration of i
*/

const threeSum = function(nums){
    // declare a new array to store the result
    let res = [];
    // sort the array in increasing order
    nums = nums.sort((a,b) => {
        return a - b;
    });
    // store the nums.lenghth which can be used frequently later
    const _len = nums.length;
    // iterate the array and note that the limit should be the last third index
    for(let i = 0; i < _len - 2; i++){
        // two pinters: i and j. j is the next index of current data while k is the last index
        let j = i + 1;
        let k = _len - 1;
        // neighbour data are the same, just skip it
        if(i > 0 && nums[i] === nums[i-1]){
            continue;
        }
        // use while to loop and the condition is j must smaller than k
        while(j < k){
            // if the sum is smaller than 0, we should move forward the former pointer
            if(nums[i] + nums[j] + nums[k] < 0){
                j++;
                // then compare the new data and the old data, if these two data are same, continue updating the pointer
                while(j < k && nums[j] === nums[j-1]){
                    j++;
                }
                // if the sum is bigger than 0, we should move back the back pointer
            }else if(nums[i]+nums[j]+nums[k] > 0){
                k--;
                // then compare the new data and the old data, if these two data are same, continue updating the pointer
                while(j < k && nums[k] === nums[k+1]){
                    k--;
                }
                // if the sum is equal to 0, just push the data to the ouput array
            }else{
                res.push([nums[i],nums[j],nums[k]]);

                // update the pointers at the same time
                j++;
                k--;

                // handle the special scenario
                while(j < k && nums[j] === nums[j-1]){
                    j++;
                }

                while(j < k && nums[k] === nums[k+1]){
                    k--;
                }
            }
        }
    }
    return res;
};