'''
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
'''
# 定义双向链表节点
class Node:
    # slots 可以节省内存空间，避免为每个实例创建 __dict__ 属性
    __slots__ = 'prev', 'next', 'key', 'value'
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity # 缓存容量
        self.dummy = Node() # 定义一个虚拟头节点，方便操作
        self.dummy.prev = self.dummy # 虚拟头节点的前驱指向自己
        self.dummy.next = self.dummy # 虚拟头节点的后继指向自己
        self.key_to_node = {} # 定义一个字典，存储 key 到节点的映射
    
    def get_node(self, key):
        if key not in self.key_to_node: # 如果 key 不在字典中，说明缓存中没有该 key，返回 None
            return None
        node = self.key_to_node[key] # 获取节点
        self.remove(node) # 将节点从链表中移除
        self.push_front(node) # 将节点插入到链表头部，表示该节点最近被使用过
        return node
    
    # 将节点从链表中移除
    def remove(self, x): 
        x.prev.next = x.next # 将节点的前驱节点的后继指向节点的后继
        x.next.prev = x.prev # 将节点的后继节点的前驱指向节点的前驱

    # 将节点插入到链表头部
    def push_front(self, x): 
        x.prev = self.dummy # 将节点的前驱指向虚拟头节点
        x.next = self.dummy.next # 将节点的后继指向原本的头节点
        x.prev.next = x # 将虚拟头节点的后继指向该节点
        x.next.prev = x # 将原本的头节点的前驱指向该节点

    # 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
    def get(self, key: int) -> int:
        node = self.get_node(key) # 获取节点
        return node.value if node else -1 # 如果节点存在，返回节点的值，否则返回 -1
        
    # 如果 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value
    def put(self, key: int, value: int) -> None:
        node = self.get_node(key) # 获取节点
        if node:
            node.value = value # 如果节点存在，更新节点的值
            return
        self.key_to_node[key] = node = Node(key, value) # 如果节点不存在，创建一个新的节点，并将其加入字典
        self.push_front(node) # 将节点插入到链表头部，表示该节点最近被使用过
        if len(self.key_to_node) > self.capacity: # 如果缓存容量超过限制，删除链表尾部的节点
            tail_node = self.dummy.prev # 获取链表尾部的节点
            del self.key_to_node[tail_node.key] # 从字典中删除该节点
            self.remove(tail_node) # 从链表中删除该节点


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)