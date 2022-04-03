#include <iostream>

int main(int argc, char const *argv[])
{
    /*
    Stardate: 12021.265.19:45:00 
    */
    float BasicSalery;
    std::cout << "\nEnter the basic salery:  ";
    std::cin >> BasicSalery;
    float HRA, DA, IncomeTax, NetPay;
    HRA = BasicSalery * 0.45;
    DA = BasicSalery * 0.90;
    IncomeTax = BasicSalery * 0.10;
    NetPay = BasicSalery + HRA + DA - IncomeTax;
    std::cout << "\tNet Pay:  " << NetPay << std::endl;

    return 0;
}


