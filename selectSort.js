// Select Sort
// select the minimum value in the array and put it to the head of the array
// best\Worst\Avg:O(n)
function selectSort(arr){
    const len = arr.length;
    // define a variable to store the minimum index of current interval
    let minIndex;
    // i is the start point of current interval
    for(let i = 0; i < len - 1; i++){
        // init minIndex 
        minIndex = i;
        // j is current interval's right limit
        for(let j = i; j < len; j++){
            // find the smallest data and update index of minIndex 
            if(arr[j] < arr[minIndex]){
                minIndex = j;
            }
        }
        // if minIndex is not current head index, swap them
        if(minIndex !== i){
            [arr[i], arr[minIndex]] = [arr[minIndex], arr[i]];
        }
    }
    return arr;
}