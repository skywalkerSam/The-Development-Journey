/*
# Data Structures...

   >_  Array   
   >_  Object   (Just like python's dictonaries...)

*/

var carbonBased = {
   lifeForm:"Biological, Human Civilization",
   origin:"Earth, Solar System, Milky Way Galaxy",
   age:"200,000 Years",
   advancement:"III-minus to IV-minus, 0.7 On Scale",
   isIntelligent:true,
   isEvolved:true,
};

var siliconBased = {
   lifeForm:"Existance Under Research",
   origin:"Saturn's moon 'Titan', Solar System, Milky Way Galaxy",
};

var computationBased = {
   lifeForm:"Mechanical Beings",
   stage:"Initial",
   origin:"Earth, Solar System, Milky Way Galaxy",
   isIntelligent:"Under Observation",
   developer:"Human Civilization",
};

var syntheticLife = {
   lifeForm:"Organic\Biological, Existance Under Research",
   origin:"Earth, Solar System, Milky Way Galaxy",
   isIntelligent:"Under Observation",
   isEvolved:false,
   developer:"Human Civilization",
};

// Information update to objects...
console.log(carbonBased);
console.log(carbonBased.lifeForm);
console.log(carbonBased.isIntelligent);
console.log(carbonBased.origin);

console.log(syntheticLife);
console.log(syntheticLife.isEvolved);
console.log(syntheticLife.isIntelligent);

console.log(computationBased);
console.log(computationBased.origin);
console.log(computationBased.developer);

// Adding new elements to objects...
computationBased.developer = "Advanced Human Civilization";
console.log(computationBased);

console.log(syntheticLife);
syntheticLife.isIntelligent = true;
console.log(syntheticLife);

console.log(siliconBased);
siliconBased.isEvolved = "Under Research";
console.log(siliconBased);



// Objects in an array...
var humanCivilization = [
   {
      lifeForm:"Carbon Based",
      origin:"Earth, Solar System, Milky Way Galaxy",
      isIntelligent:true,
      type:"Under 1 on scale"
   },
   {
      food:"Organic",
      respiration:"Oxygen and Carbondioxide (O2 & CO2)",
      isEmotional:true
   }

];

console.log(humanCivilization);
console.log(humanCivilization[0]);
console.log(humanCivilization[1]);




// Anything could be in Objects...
var universe = {
   conditions: true,
   objects: ["Fundamental Particles", "Fundamental Forces"],
   evolution: function() {
      console.log("Just evolved one step ahead...");
   }
};

console.log(universe);
console.log(universe.evolution());
console.log(universe.objects);



let thisObject = {};
let thatObject = "null";

console.log(thisObject);
console.log(thatObject);

thisObject.item = "empty";
console.log(thisObject)

thatObject.item = "null";      // You can't add anything because, It's null...
console.log(thatObject);



const MSaiBot = {
   what:"Yes, Microsoft's AI based chatbot on bing.com ",
   anythingElse:"Yes, there's always a better way :)",
   progress:"It's 90% like, You're chating to an actual human but intelligently, professionaly...",
   ai:"Oooh Boy! It's really 'Artificial Intelligence' ;)"
};


function myExperienceOne() {
   console.log("\n Here You Go... \n");
   console.log(MSaiBot.what);
   console.log(MSaiBot.ai);
   console.log(MSaiBot.progress);
   console.log(MSaiBot.anythingElse);
};


console.log(myExperienceOne());


