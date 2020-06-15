// there are two methods for throttle
// the first one is called time stamp and the second one is timer

// time stamp

var throttle = function(func, delay){
    // previous time when bind to the event
    var prev = Date.now();
    // actual events happened are in the enclosure 
    return function(){
        var context = this;
        var args = arguments;
        // current time
        var now = Date.now();
        if (now - prev >= delay){
            // operation
            func.apply(context, args);
            prev = Date.now();
        }
    }
}


function handle(){
    console.log(Math.round(Math.random() * 10));
}

window.addEventListener('scroll',throttle(handle,1000));


// timer version
var throttle2 = function(func,delay){
    // define a empty timer
    var timer = null;
    // actual events happened are in the enclosure 
    return function(){
        var context = this;
        var args = arguments;
        // if the timer is null, set the timer
        if(!timer) {
            timer = setTimeout(function(){
                // operation
                func.apply(context, args);
                // once we have finished the operation, clear the timer
                timer = null;
            }, delay);
        }
    }
}

function handle2(){
    console.log(Math.round(Math.random() * 10));
}

window.addEventListener('scroll',throttle2(handle2,1000));


// Advanced version: time stamp + timer
var throttle3 = function(func,delay){
    // define timer and initial time stamp
    var timer = null;
    var startTime = Date.now();
    // use closure
    return function(){
        // get current time when the event happened
        var curTime = Date.now();
        var remaining = delay - (curTime - startTime);
        var context = this;
        var args = arguments;
        clearTimeout(timer);
        if(remaining <= 0){
            func.apply(context,args);
            startTime = Date.now();
        }else{
            timer = setTimeout(func, remaining);
        }
    }
}

function handle3(){
    console.log(Math.round(Math.random() * 10));
}

window.addEventListener('scroll',throttle3(handle3,1000));