#include <iostream>

int main(int argc, char const *argv[])
{
    /*
    Stardate: 12021.265.20:00:00 
    */
    int number;
    std::cout << "\nEnter the number:  ";
    std::cin >> number;

    if (number % 5 == 0)
    {
        std::cout << "\tIt's divisibe by 5 :)\n";
    }
    else 
    {
        std::cout << "\tIt's NOT divisibe by 5 :(\n";
    }

    return 0;
}


