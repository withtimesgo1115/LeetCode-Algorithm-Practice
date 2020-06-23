const leftToRight = {
    "(": ")",
    "[": "]",
    "{": "}"
};

const isValid = function(s){
    // empty string return true
    if(!s){
        return true;
    }
    // init a stack
    const stack = [];
    // store the length of the string
    const len = s.length;
    // iterate the string
    for(let i = 0; i < len; i++){
        // store current character in the string
        const ch = s[i];
        // judege if current char is left bracket
        // if true, push corresponding right char to the stack
        if(ch === "(" || ch === "{" || ch === "["){
            stack.push(leftToRight[ch]);
            // if it is not left bracket, then it must be a right
            // bracket which can match left bracket on the top of the stack
        }else{
            // if stack is empty or the left bracket on the stack's top position
            // cannot match current char, return false  
            if(!stack.length || stack.pop() !== ch){
                return false;
            }
        }
    }

    // if all the brackets can match, then the stack should be empty finally
    return !stack.length;
};