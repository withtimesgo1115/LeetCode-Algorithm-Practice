// constructor
const WorldDictionary = function(){
    this.words = {}
};

// add word method
WorldDictionary.prototype.addWord = function(word){
    // if the corresponding length's array exists, just add word
    if(this.words[word.length]){
        this.words[word.length].push(word);
    }else{
        // else create the array
        this.words[word.length] = [word];
    }

};

// search method
WorldDictionary.prototype.search = function(word){
    // if there is no array with this length, return false
    if(!this.words[word.length]){
        return false;
    }
    // store the length
    const len = word.length;
    // if there is no '.' in the string
    if(!word.includes('.')){
        // judge if there is the word in the string
        return this.words[len].includes(word);
    }
    
    // else it is a RegExp so that we should create a new object 
    const reg = new RegExp(word);

    // if there is a string which can match the reg expression
    // then return true
    // Array.prototype.some() will return a boolean value to check if there is an item meeting the requirements in the arrow function
    return this.words[len].some((item) => {
        // judge if the item is the same with reg
        return reg.test(item);
    })

};