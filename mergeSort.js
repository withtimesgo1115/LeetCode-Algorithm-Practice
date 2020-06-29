function mergeSort(arr){
    const len = arr.length;
    // handle borders
    if(len <= 1){
        return arr;
    }
    // calc dividing point
    const mid = Math.floor(len / 2);
    // divide left sub-array in recursion way and then merge them to sorted array
    const leftArr = mergeSort(arr.slice(0,mid));
    // divide right sub-array in recursion way and then merge them to sorted array
    const rightArr = mergeSort(arr.slice(mid,len));
    // merge two sorted arrays
    arr = mergeArr(leftArr, rightArr);
    // return the result
    return arr;
}

function mergeArr(arr1,arr2){
    // init two pointers
    let i = 0, j = 0;
    // init a new array to store the merged array
    const res =[];
    const len1 = arr1.length;
    const len2 = arr2.length;
    // use while loop to merge two ordered arrays
    while(i < len1 && j < len2){
        if(arr1[i] < arr2[j]){
            res.push(arr[i]);
            i++;
        }else{
            res.push(arr2[j]);
            j++;
        }
    }
    // if certain one subarray has been merged already then concatenate the other subarray to the left position
    if(i < len1){
        return res.concat(arr1.slice(i));
    }else{
        return res.concat(arr2.slice(j));
    }
}