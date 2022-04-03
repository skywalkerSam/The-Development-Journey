/***************************************************
Author: Sam Skywalker
Purpose: Learning the C++ basics
Date: 12022.01.06.05:22

****************************************************/


#include <iostream>     // Preprocessor Directives...

/*

    *Namespace     -> To avoid conflicts from different libraries, we use "std::cout". It could be "asai::cout" or "google::cout".. Different versions of "cout" are defined by different libraries...

>_  " using namespace std; "    -> You're no longer required to do "std::" but, It could be conflicted over large programs.

    // So, We've to be more specfic ;)

>_  " using std::cout; " 
>_  " using std::cin; "     // Use only what you need, Ok :)
>_  " using std::endl; " 


*/


int main()      // Main Function()
{
    int number_one;     // Reserved Keywords (int, return, etc.)
    std::cout<<std::endl<<"Enter a number: ";
    std::cin>>number_one;
    std::cout<<number_one<<", Hey! that's my favorite number.. "<<std::endl;


    return 0;   // The main() should must return, just like other functions...
}



/*
# C++ Standards: C++98, C++03
# Modern C++: C++11, C++14, C++17, C++20

*/
