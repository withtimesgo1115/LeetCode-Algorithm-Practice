// input is index range, low is min limit, high is max limit
function downHeap(low, high){
    // init i as current node and j is current node's left child
    let i = low, j = i * 2 + 1;
    // if j is smaller than the upper limit, do comparing and swapping again and again
    while(j <= high){
        // downward should consider two children but upward should not consider that because there is only one parent node
        // if right child is larger than left child, 
        if(j + 1 <= high && heap[j+1] > heap[j]){
            j = j + 1;
        }

        // if current node is smaller than child node, swap them
        if(heap[i] < heap[j]){
            // swap position
            const temp = heap[j];
            heap[j] = heap[i];
            heap[i] = temp;

            // i is updated 
            i = j;
            // update j
            j = j * 2 + 1;
        }else{
            break;
        }
    }
};

// input parameters is the index range of the array, low is the bottom limit, high is the upper limit
function upHeap(low, high){
    // current  index is the upper limit
    let i = high;
    // init j as i's parent node
    let j = Math.floor((i - 1) / 2);
    // if parent node's index is lower than the bottom limit, loop again and again
    while(j >= low){
        // if current node is bigger than parent node
        if(heap[j] < heap[i]){
            // swap them
            const temp = heap[j];
            heap[j] = heap[i];
            heap[i] = temp;

            // update i to parent node: go up of the layer
            i = j;
            // update j to parent node's parent node
            j = Math.floor((i - 1) / 2);
        }else{
            // if current node is smaller than its parent node
            // just break the loop
            break;
        }
    }
}