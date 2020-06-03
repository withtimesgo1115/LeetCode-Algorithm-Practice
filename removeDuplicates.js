// This is an algorithm written in JS to remove duplicates
// O(n*n)
function unique(arr){
    // iterate the array
    for(var i=0;i<arr.length;++i){
        // iterate the array from the second element
        for(var j = i + 1; j < arr.length;++j){
            // compare current element and the next one
            if(arr[i] === arr[j]){
                // remove duplicate using arr.splice(j,1) from j remove one element
                arr.splice(j,1);
            }
        }
    }
    return arr;
}