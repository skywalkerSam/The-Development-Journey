
let fruitsList = ['Bananas', 'Apples', 'Oranges', "Blueberries"];

// 1
console.log(fruitsList);
fruitsList.shift('Bananas');
console.log(fruitsList);

// 2
fruitsList.sort();
console.log(fruitsList);

// 3
fruitsList.push('kiwi');
console.log(fruitsList);

// 4
// fruitsList.shift();      // There's always a better way...
fruitsList.splice(0, 1)
console.log(fruitsList);

// 5
fruitsList.reverse();
console.log(fruitsList);

// Array-Two
var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

console.log(array2[0]);
console.log(array2[1]);

console.log(array2[0][1]);
console.log(array2[1][0]);

console.log(array2[1][1]);
console.log(array2[1][1][0]);




