var merge = function(nums1, m, nums2, n) {
    // define three pointers pointing to 3 position
    // i points to the last meaningful data in array 1
    // j points to the last data in array 2
    // k points to the last position in array 1
    var i = m - 1;
    var j = n - 1;
    var k =  m + n - 1;
    // work only when i and j are larger than or euqal to 0
    while(i >= 0 && j >= 0){
        // the data in the nums1[i] is larger
        // assign data to the num1[k] and move pointer i and k
        if(nums1[i] >= nums2[j]){
            nums1[k] = nums1[i];
            i--;
            k--;
        }
        // the data in the nums2[j] is larger
        // assign data to the nums1[k] and move pointer j and k
        else{
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
    // when array 1 has been checked to the first data
    // but the array 2 still has data and these data can be 
    // added to the head of the array 1 so we can use while loop
    while(j>=0){
        nums1[k] = nums2[j];
        k--;
        j--;
    }
};