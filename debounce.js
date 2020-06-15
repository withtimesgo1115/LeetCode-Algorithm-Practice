function debounce(fn, wait){
    // define a timer and its initial value is null
    var timeout = null;
    // use a clousure to achieve the goal and access the timer
    return function(){
        // if timer exists, clear current timer
        if(timeout !== null){
            clearTimeout(timeout);
        }
        // if timer doesn't exist, set the timer again
        timeout = setTimeout(fn, wait);
    }
}

// operation function
function handle(){
    console.log(Math.round(Math.random() * 10));
}

// scroll event
window.addEventListener('scroll', debounce(handle, 1000));

/*

if we don't have debounce, the callback operation will work once the event
is called

window.addEventListener('scroll', function(){
    setTimeout(handle,1000)
});
*/




