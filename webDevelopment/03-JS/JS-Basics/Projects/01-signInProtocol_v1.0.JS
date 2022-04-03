/*
Developer: Sam Skywalker
Purpose: Developing the signIn Protocol...
Date: 12022.01.20.22:47
*/

let userDatabase = [
    {
        username:"sam",
        password:"FionaIsAwesome",
    },
    {
        username:"skywalkerSam",
        password:"AlitaTheBattleAngel",
    },
    {
        username:"starboy",
        password:"StargirlForStarboy",
    },
    {
        username:"master-skywalker",
        password:"TrisDauntless",
    }
];


userNewsfeed = [
    {
        username:"starboy",
        newsfeed:"Nothing can tell you more than stars...",
    },
    {
        username:"sam",
        newsfeed:"Good or, bad are just the matter of perspective..."
    },
];



/*
// For Browsers...
usernamePrompt = prompt("Enter Your Username... \n");
passwordPrompt = prompt("Enter Your Password... \n");
*/


// For Node.js console...
// Custom node module 'prompt-sync' to get input truough node.js console...
const prompt = require("prompt-sync")({ sigint: true });
const usernamePrompt = prompt("Enter Your Username... \n");
const passwordPrompt = prompt("Enter Your Password... \n");
// console.log(`You are ${age} years old.`);


function signIn(user, pass) {
    if (user === userDatabase[0].username && pass === userDatabase[0].password) {
        console.log(userNewsfeed);
    } else {
        console.log("\t Wrong Username or, Password. Please Try Again! \n")
    }
}


signIn(usernamePrompt, passwordPrompt)




/*
01- Node.js Module Installation...

    >_ npm install "ModuleName"     ( 1st, Go to the working directory )


02- Some Node Console Commands...

    >_  node

    >_  node "FileName.js"

    >_  .exit

    >_  .editor

*/


// I'm using node.js console in VScode with codeRunner instead of browser console to run JS codes...
