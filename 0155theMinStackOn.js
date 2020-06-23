/**
 * initialize your data structure here.
 */
var MinStack = function() {
    this.stack = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MinStack.prototype.push = function(x) {
    this.stack.push(x);
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    if(this.stack.length !== 0){
        return this.stack[this.stack.length - 1];
    }else{
        return null;
    }
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    let minVal = Infinity;
    for(let i = 0; i < this.stack.length; ++i){
        if(this.stack[i] < minVal){
            minVal = this.stack[i];
        }
    }
    return minVal;
};