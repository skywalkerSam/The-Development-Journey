//carIntro()
var carIntro = function() {
    console.log("Hello, I'm your car :)")
}



//checkDriverAge()
function checkDriverAge(age=0) {
    if (age >= 18) {
        console.log("Enjoy your ride :)");
    } else if (age === 0) {
        console.log("Please verify you age...");
    } else {
        console.log("Sorry, You're too young to drive this car :(");
    }
}

checkDriverAge(90)

