#include <iostream>

int main(int argc, char const *argv[])
{
    /* Stardate: 12021.263.15:14:00 */
    float price;
    std::cout << "\nEnter the price of one:  ";
    std::cin >> price;
    float number;
    std::cout << "Enter the number of stuff:  ";
    std::cin >> number;
    float TotalPrice = price * number;
    std::cout << "\tThe total price:  " << TotalPrice << std::endl;

    return 0;
}




