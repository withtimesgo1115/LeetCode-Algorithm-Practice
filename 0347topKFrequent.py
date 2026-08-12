'''
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

 

示例 1：

输入：nums = [1,1,1,2,2,3], k = 2

输出：[1,2]

示例 2：

输入：nums = [1], k = 1

输出：[1]

示例 3：

输入：nums = [1,2,1,2,1,2,3,1,3,2], k = 2

输出：[1,2]


'''
# 用最小堆实现
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = {} # 统计每个元素的频率
        for num in nums:
            if num in frequencyMap:
                frequencyMap[num] += 1
            else:
                frequencyMap[num] = 1
        
        minHeap = [] # 创建一个最小堆，堆中存储频率和对应的元素
        # 遍历频率字典，将频率和对应的元素加入到最小堆中
        for num, freq in frequencyMap.items():
            # 如果最小堆的大小小于 k，则直接将当前元素加入到最小堆中
            if len(minHeap) < k:
                heapq.heappush(minHeap, (freq, num))
            # 如果最小堆的大小等于 k，则比较当前元素的频率和最小堆堆顶元素的频率
            elif freq > minHeap[0][0]:
                heapq.heappushpop(minHeap, (freq, num))
        # 将最小堆中的元素取出，得到出现频率前 k 高的元素
        topK = [num for _, num in minHeap]
        return topK



        