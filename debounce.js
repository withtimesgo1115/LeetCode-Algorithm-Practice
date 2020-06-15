function debounce(fn, wait){
    var timeout = null;
    return function(){
        if(timeout !== null){
            clearTimeout(timeout);
        }
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




