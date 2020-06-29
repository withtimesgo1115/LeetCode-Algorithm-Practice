/* Solutio 1 easy 
const findKthLargest = function(nums,k){
    const sorted = nums.sort((a,b) => {
        // sort from minimum to maximum
        return b - a;
    });
    return sorted[k - 1];
};
*/

// Solution 2 difficult but powerful
// use Heap!

const findKthLargest = function(nums, k){
    const heap = [];
    let n = 0;
    const len = nums.length;
    
    function createHeap(){
        for(let i = 0; i < k; i++){
            insert(nums[i]);
        }
    };

    // 插入操作=将元素添加到堆尾部+向上调整元素的位置
    function insert(x) {
        heap[n] = x;
        upHeap(0, n);
        n++;
    };

    function updateHeap(){
        for(let i = k; i < len; ++i){
            // 只有比堆顶元素大的才有资格进堆
            if(nums[i] > heap[0]){
                // 用较大数字替换堆顶数字
                heap[0] = nums[i];
                // 重复向下对比+交换的逻辑
                downHeap(0,k);
            }
        }
    };

    function downHeap(low, high){
        // 入参是堆元素在数组里的索引范围，low表示下界，high表示上界
        let i = low, j = 2 * i + 1;
        // 当 j 不超过上界时，重复向下对比+交换的操作
        while(j <= high){
            // 如果右孩子比左孩子更小，则用右孩子和根结点比较
            if(j + 1 <= high && heap[j+1] < heap[j]){
                j = j + 1;
            }

            // 若当前结点比孩子结点大，则交换两者的位置，把较小的结点“拱上去”
            if(heap[i] > heap[j]){
                const temp = heap[j];
                heap[j] = heap[i];
                heap[i] = temp;

                 // i 更新为被交换的孩子结点的索引
                i = j;
                // j 更新为孩子结点的左孩子的索引
                j = j * 2 + 1;
            }else{
                break;
            }
        }     
    };

    function upHeap(low, high){
        // 初始化 i（当前结点索引）为上界
        let i = high;
        // 初始化 j 为 i 的父结点
        let j = Math.floor((i - 1) / 2);
        // 当 j 不逾越下界时，重复向上对比+交换的过程
        while(j >= low){
            // 若当前结点比父结点小
            if(heap[j] > heap[i]){
                // 交换当前结点与父结点，保持父结点是较小的一个
                const temp = heap[j];
                heap[j] = heap[i];
                heap[i] = temp;

                // i更新为被交换父结点的位置
                i = j;
                // j更新为父结点的父结点
                j = Math.floor((i - 1) / 2);
            }else{
                break;
            }
        }
    };

    // 调用createHeap初始化元素个数为k的队
    createHeap();
    // 调用updateHeap更新堆的内容，确保最后堆里保留的是最大的k个元素
    updateHeap();
    // 最后堆顶留下的就是最大的k个元素中最小的那个，也就是第k大的元素
    return heap[0];
}

