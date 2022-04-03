 /*
    Developer: Master Skywalker
    Purpose: Project-GameOne
    Stardate: 12021.255.19:45:00
*/

#include <iostream>


// User Defined Functions
void GameIntro(int Difficulty)
{
    std::cout << "\n\t\t\"ASAI's Research Lab Is Under Attack, Break The Codes To Get Into The 'Level "<< Difficulty; 
    std::cout << "' Secured Datacentre Facility, Cut The Hard Line & Save The Research Data From Going Into The Wrong Hands...\"\n\n\n";

}


bool PlayGame()     // bool must return boolean...
{
    GameIntro(9);

    int CodeA = 3;
    int CodeB = 6;
    int CodeC = 9;

    int CodeSum = CodeA + CodeB + CodeC;
    int CodeProduct = CodeA * CodeB * CodeC;

    std::cout << ">_    Here's Some Informations About The Code...\n\n";
    std::cout << "+ The Total Numbers Of Code: 3\n";
    std::cout << "+ The Codes Join Upto: " << CodeSum << std::endl;
    std::cout << "+ The Codes Product Upto: " << CodeProduct << std::endl;

    int GuessA, GuessB, GuessC;
    std::cout << "\n\tNow, Enter The Codes: ";
    std::cin >> GuessA >> GuessB >> GuessC;
    
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    if (GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\n\t\t\t Welcome To The ASAI'S Datacentre Facility :)\n\n";
        return true;
    }   
    else
    {
        std::cout << "\n\t\t Alert! There's A Breach In The Datacentre Facility :(\n\n";
        // std::cout << "\tWell, The Codes Were: " << CodeA << CodeB << CodeC << std::endl;
        return false;
    }

}


// Main Function
int main(int argc, char const *argv[])
{   
    int LevelDifficulty = 1;    // Remember The Variable Scope...

    // While Loop
    while (true)
    {   
        bool bLevelComplete = PlayGame();
        std::cin.clear();   // Clears any error...
        std::cin.ignore();  // Discard the buffer...
        if (bLevelComplete)

        {
            ++LevelDifficulty;    // LevelDefficulty = LevelDifficulty + 1
        }
        
        
    }

    return 0;
}



