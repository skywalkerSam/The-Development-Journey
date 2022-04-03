#include <iostream>

int main(int argc, char const *argv[])
{
    /* code */
    float length;
    std::cout << "\nEnter the length:  ";
    std::cin >> length;
    float width;
    std::cout << "Enter the width:  ";
    std::cin >> width;
    double area;
    area = length * width;
    std::cout << "\tThe area of your rectangle:  " << area << std::endl ;

    return 0;
}
