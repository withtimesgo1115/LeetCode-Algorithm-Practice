/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stack = [];
    // define a support stack to store the minimum values
    this.stack2 = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.stack.push(x);
    // if support stack is empty or current data is smaller than current minimum
    // add this data to the support stack too
    if(this.stack2.length == 0 || this.stack2[this.stack2.length-1] >= x){
        this.stack2.push(x);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    // if the data poped out is equal to current minimum, then the support stack
    // should pop the top data to ensure the validity of minimum
    if(this.stack.pop() === this.stack2[this.stack2.length-1]){
        this.stack2.pop();
    }
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length-1];
};

/**
 * @return {number}
 */

MinStack.prototype.getMin = function() {
    // support stack's top position
    // stores the minimum value
    return this.stack2[this.stack2.length-1];
};