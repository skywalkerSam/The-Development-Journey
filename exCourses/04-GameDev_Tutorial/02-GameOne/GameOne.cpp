 /*
    Developer: Master Skywalker
    Purpose: Project-GameOne
    Stardate: 12021.255.19:45:00
*/

#include <iostream>
#include <ctime>


// User Defined Functions
void GameIntro(int Difficulty)
{
    std::cout << "\n\t AIM : \n\t***  ASAI's Research Lab Is Under Attack, Break The Codes To Get Into The 'LEVEL "<< Difficulty; 
    std::cout << "' Secured Datacentre Facility, Cut The Hard Line & Save The Research Data From Going Into The Wrong Hands...  *** \n\n\n";

}


bool PlayGame(int Difficulty)     // bool must return boolean...
{
    GameIntro(Difficulty);

    int CodeA = rand() % Difficulty + Difficulty;    //  rand() genrates values upto 32000. To get smaller values, we're using modulo operator...
    int CodeB = rand() % Difficulty + Difficulty;    //  "Difficulty + Difficulty" to make it much difficult...
    int CodeC = rand() % Difficulty + Difficulty;    //  " +1 " to remove any 0 values & make it more difficult...

    int CodeSum = CodeA + CodeB + CodeC;
    int CodeProduct = CodeA * CodeB * CodeC;

    std::cout << ">_    Here's Some Informations About The Code...\n\n";
    std::cout << "+ The Total Series Of Code:   3  ( X X X )\n";
    std::cout << "+ The Codes Join Upto:        " << CodeSum << std::endl;
    std::cout << "+ The Codes Product Upto:     " << CodeProduct << std::endl;

    int GuessA, GuessB, GuessC;
    std::cout << "\n\tNow, Enter The Codes: ";
    std::cin >> GuessA >> GuessB >> GuessC;
    
    int GuessSum = GuessA + GuessB + GuessC;
    int GuessProduct = GuessA * GuessB * GuessC;

    if (GuessSum == CodeSum && GuessProduct == CodeProduct)
    {
        std::cout << "\n\t\t\t ###   Welcome To The ASAI'S 'LEVEL "<< Difficulty;
        std::cout << "' Datacentre Facility :)   ### \n\n";
        return true;
    }   
    else
    {
        std::cout << "\n\t\t ###   Alert! There's A Breach In The 'LEVEL "<< Difficulty;
        std::cout << "' Datacentre Facility :(   ### \n\n";
        // std::cout << "\tWell, The Codes Were: " << CodeA << CodeB << CodeC << std::endl;
        return false;
    }

}


// Main Function
int main(int argc, char const *argv[])
{   
    srand(time(NULL));     // More complex random numbers based on time of the day...

    int LevelDifficulty = 1;    // Remember The Variable Scope...
    const int MaxDifficulty = 5;

    // While Loop
    while (LevelDifficulty <= MaxDifficulty)
    {   
        // std::cout << rand() % 5 << '\n';
        bool bLevelComplete = PlayGame(LevelDifficulty);
        std::cin.clear();   // Clears any error...
        std::cin.ignore();  // Discard the buffer...

        if (bLevelComplete)
        {
            ++LevelDifficulty;    // LevelDefficulty = LevelDifficulty + 1
        }
        else
        {
            std::cout << "\n ###   You've Entered An Incorrect Code :(  After One More Unsuccessful Attempt, Lockdown Procedures Will Be Initiated...  ### \n\n";
        }
        
    }
    std::cout << "\n ###   You've Saved The ASAI's Research Lab Today, You're Awesome :)   ### \n\n";
    return 0;
}






