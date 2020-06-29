// best:O(n) worst:O(n^2) avg:O(n^2)

function insertSort(arr){
    // store the length of the array
    const len = arr.length;
    // temp is used to store current element which should be interted
    let temp;
    // i is used to mark the data which should be inserted
    for(let i = 0; i < len; ++i){
        // j is used to help temp find its position
        // from rear to the former
        let j = i;
        temp = arr[i];
        // judge j's former element if it is bigger than temp
        while(j > 0 && arr[j-1] > temp){
            // if true, j-1 moves back one position to make space for temp
            arr[j] = arr[j-1];
            j--;
        }
        // make space in the loop, so j is the correct index of temp in the end
        arr[j] = temp;
    }
    return arr;
}