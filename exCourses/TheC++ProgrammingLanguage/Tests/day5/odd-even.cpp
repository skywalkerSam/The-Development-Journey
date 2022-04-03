#include <iostream>

int main(int argc, char const *argv[])
{
    /*
    Stardate: 12021.265.20:00:00 
    */
    int number;
    std::cout << "\nEnter the number:  ";
    std::cin >> number;
    
    if (number % 2 == 0)
    {
        std::cout << "\tIt's an even number...\n";
    }
    else 
    {
        std::cout << "\tIt's an odd number...\n";
    }


    return 0;
}

