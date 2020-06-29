// Bubble sort
// Best:O(n) Worst:O(n^2) Average:O(n^2) 

function bubbleSort(arr){
    const len = arr.length;
    for(let i = 0; i < len; i++){
        for(let j = 0; j < len - 1;){
            if(arr[j] > arr[j+1]){
                // ES6 syntax
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
            }
        }
    }
    return arr;
}

function betterBubbleSort(arr){
    const len = arr.length;
    for(let i = 0; i < len; ++i){
        // difference here!
        for(let j = 0; j < len - 1 - i; ++j){
            if(arr[j] > arr[j+1]){
                [arr[j],arr[j+1]] = [arr[j+1],arr[j]];
            }
        }
    }
    return arr;
}

// the best scenario: O(n) 
function bestBubbleSort(arr){
    const len = arr.length;

    for(let i = 0; i < len; ++i){
        let flag = false;
        for(let j = 0; j < len - 1 - i; ++j){
            if(arr[j] > arr[j+1]){
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
                flag = true;
            }
        }

        if(flag === false) return arr;
    }
}
