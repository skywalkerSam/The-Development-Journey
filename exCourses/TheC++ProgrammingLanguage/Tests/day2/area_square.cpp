#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    float side;
    std::cout << "\nEnter the side:  ";
    std::cin >> side;
    double area = side * side;
    std::cout << "\tThe area of your square:  " << area << std::endl;


    return 0;
}


