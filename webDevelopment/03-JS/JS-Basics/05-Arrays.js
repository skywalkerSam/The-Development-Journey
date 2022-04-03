// Data Structures...

//      #1- Array   (Like, python's list[])
//      #2- Object

console.log("Hello World... \n");

var wotd = "Hola! soy Sam."


var first_array = ["You can put anything in here.", "Just like python's list..", "Index starts with 0 again...", "You can store functions() too....", 01, true, false, ":)"];

// console.log(first_array);
console.log(first_array[7]);
console.log(first_array[1]);    // Semicolons aren't effecting the code...



function spanishCounting() {
    var spanish_counting = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez"];      // Array
    return spanish_counting;
}

// console.log(spanishCounting())



var array_dos = [spanishCounting(), "Dos Oruguitas", 2, "Oruguitas", wotd];
console.log(array_dos);
console.log("Who are you?   ", array_dos[4], "Mucho Gusto.. \n");
console.log(array_dos[0]);



// Matrix Array...      (Something just like numpy)

var matrixArray = [
    ["zero", "one", "two", "three"],
    ["cero", "uno", "dos", "tres"]
];
console.log(matrixArray[0][1]);
console.log(matrixArray[1][2]);



// Array Functions..

simpleArray = ["civilizations", "planets", "moons", "stars"];
console.log(simpleArray);

simpleArray.shift();
console.log(simpleArray);

simpleArray.pop();
console.log(simpleArray);

simpleArray.push("Universe");
console.log(simpleArray);

simpleArray.concat(["Aliens", "Nihilism"]);   // It doesn't modify the original array, It creates a copy which you can assign to a variable...
console.log(simpleArray);

simpleArray.sort();
console.log(simpleArray);

simpleArray.push("Aliens", "Nihilism");
simpleArray.sort()
console.log(simpleArray);

var simpleArray = simpleArray.concat(["Spacefaring Civilizations", "The Legendary, 'Simulation Argument'..."]);
console.log(simpleArray)



/* 
# Wanna know more?     
    >_  Don't forget about your google and w3schools ;)
    >_  Search "Javascript array functions"

*/
