#include <iostream>

int main(int argc, char const *argv[])
{
    /*
    Stardate: 12021.265.19:45:00 
    */
    float CostPrice;
    std::cout << "\nEnter the cost price:  ";
    std::cin >> CostPrice;
    float profit;
    std::cout << "Enter the profit (In Decimal):  ";
    std::cin >> profit;
    float NetProfit = CostPrice * profit;
    float SalePrice = CostPrice + NetProfit;
    std::cout << "\tThe Sale Price:  " << SalePrice;


    return 0;
}




