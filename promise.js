// firstly, we should define three states for a promise: pending\resolved\rejected 
const PENDING = 'pending';
const RESOLVED = 'resolved';
const REJECTED = 'rejected';

// here we define our promise function which requires a callback function called fn as the only parameter
function MyPromise(fn) {
    // note that we need to store this pointer in order to obtain the correct this pointer since the codes may run in async way
    // define initial state, value, callback array of resolved and rejected
    const that = this;
    that.state = PENDING;
    that.value = null;
    that.resolvedCallbacks = [];
    that.rejectedCallbacks = [];

    // here we define resolve function which requires a value as parameter
    function resolve(value){
        // no matter resolve or reject, only when the state is pending, the state can change so that we used if to judge
        if(that.state === PENDING){
            // change the state and value
            that.state = RESOLVED;
            that.value = value;
            // iterate resolvedCallbacks array and run each callback based on current value 
            that.resolvedCallbacks.map(cb => cb(that.value));
        }
    }

    // here we define reject function which requires a value as parameter
    function reject(value){
        if(that.state === PENDING){
            that.state = REJECTED;
            that.value = value;
            that.rejectedCallbacks.map(cb => cb(that.value));
        }
    }

    // main logic use try firstly 
    try{
        // use callback function fn and pass both resolve and reject
        fn(resolve, reject);
        // meet error, just reject
    }catch(e){
        reject(e);
    }
}

// define promise's then function
MyPromise.prototype.then = function(onFulfilled, onRejected){
    // store this pointer
    const that = this;
    // judge if these two parameters are function. If they are function, use onFulfilled else use following
    onFulfilled = typeof onFulfilled === 'function' ? onFulfilled : v => v
    onRejected = typeof onRejected === 'function' ? onRejected : r => {
        throw r;
    }
    //if the state is pending, just push these two function to corresponding callback array
    if(that.state === PENDING){
        that.resolvedCallbacks.push(onFulfilled);
        that.rejectedCallbacks.push(onRejected);
    }
    // run onFulfilled function if the state is resolved 
    if(that.state === RESOLVED){
        onFulfilled(that.value);
    }
    // run onRejected function if the state is rejected
    if(that.state === REJECTED){
        onRejected(that.value);
    }
}