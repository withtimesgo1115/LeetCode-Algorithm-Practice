// there are two methods for throttle
// the first one is called time stamp and the second one is timer

// time stamp
/*
var throttle = function(func, delay){
    var prev = Date.now();
    return function(){
        var context = this;
        var args = arguments;
        var now = Date.now();
        if (now - prev >= delay){
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
    var timer = null;
    return function(){
        var context = this;
        var args = arguments;
        if(!timer) {
            timer = setTimeout(function(){
                func.apply(context, args);
                timer = null;
            }, delay);
        }
    }
}

function handle2(){
    console.log(Math.round(Math.random() * 10));
}

window.addEventListener('scroll',throttle2(handle2,1000));
*/

// Advanced version: time stamp + timer
var throttle3 = function(func,delay){
    var timer = null;
    var startTime = Date.now();
    return function(){
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