
// Function Declaration...
function FunctionOne() {
    console.log("It's created by Function Declaration...");     // A function() must return something...
};



// Function Expression...
FunctionTwo = function() {
    console.log("It's created by Function Expression...");
};

FunctionThree = function MatrixFunction() {
    console.log("It's a Matrix Function...");
};


// Function with parameters...
function sumFunction(numOne, numTwo) {
    return (numOne + numTwo);
};



// Expressions...
//      1+3;
//      let sam = "Developer";  
//      return true;



// Calling or, Invoking a function()...
//      alert()
//      prompt()
//      console.log()
console.log(FunctionTwo());
console.log(FunctionThree);
console.log(sumFunction(1, 2));



// function VS method...
//      function()
function thisIsAFunction() {
    console.log("\t If you'll try to build something with Vanilla.js, you'll end up building your own JS framework. And the last thing the world wants is, 'A New Javascript Framework' :) ...\n")
}

console.log(thisIsAFunction());


//      method, It's also a function() but, inside a Javascript Object :)
let objectOne = {
    thisISAMethod: function() {
        console.log("\t Yes, a function() inside an object is so called \'a method\' ...");
        console.log("\t You can access a method by 'MethodName.FunctionName()' ...");
    }
};

console.log(objectOne.thisISAMethod());


