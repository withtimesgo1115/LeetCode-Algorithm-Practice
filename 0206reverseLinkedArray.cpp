/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


 // iteration method to reverse a single-linked array O(n) in time and O(1) in space
// 输入: 1->2->3->4->5->NULL
// 输出: 5->4->3->2->1->NULL
class Solution {
public:
    // return type is ListNode* which is a pointer pointed to this kind of  node
    ListNode* reverseList(ListNode* head) {
        // define prev and curr pointers, one is nullptr and the other is pointing to the head node
        ListNode* prev = nullptr;
        ListNode* curr = head;
        // use while loop to iterate all the node if current node is not an empty node which means 
        // curr != nullptr
        while(curr != nullptr){
            // define a pointer pointed to a new node and it points to curr->next, here we don't care about the next node
            // this means the next node can be an empty node too
            ListNode* nextTemp = curr->next;
            // consider the new value of right part 
            // current->next should be the former previous element, this can also be considered as swap operation
            curr->next = prev;
            // consider the new value of right part too
            prev = curr;
            // consider the new value of right part again
            // move to the next position using nextTemp replace curr
            curr = nextTemp;
        }
        return prev;
    }
};