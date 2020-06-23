/**
 * Initialize your data structure here.
 */

// stack1 1 2 3  stack2 3 2 1 => pop: 1 2 3 
// 所有的出队操作都只能依赖 stack2 来完成

 // use two stacks to contruct queue
var MyQueue = function() {
    this.stack1 = [];
    this.stack2 = [];
};

/**
 * Push element x to the back of queue. 
 * @param {number} x
 * @return {void}
 */

// just push data to the stack1
MyQueue.prototype.push = function(x) {
    this.stack1.push(x);
};

/**
 * Removes the element from in front of queue and returns that element.
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    // stack2 is empty and satck1 is not empty so that we should add data to stack2 from stack1
    if(this.stack2.length <= 0){
        while(this.stack1.length !== 0){
            this.stack2.push(this.stack1.pop());
        }
    }
    // stack2 is not empty so that just pop here
    return this.stack2.pop();
};

/**
 * Get the front element.
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if(this.stack2.length <= 0){
        while(this.stack1.length !== 0){
            this.stack2.push(this.stack1.pop());
        }
    }
    // store the length of stack2
    const stack2Len = this.stack2.length;
    // return the last data of stack2
    return this.stack2[stack2Len - 1];
};

/**
 * Returns whether the queue is empty.
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    return !this.stack1.length && !this.stack2.length;
};