/***************************************************
Author: Sam Skywalker
Purpose: Learning the C++ basics
Date: 12022.01.06.05:22

****************************************************/

#include <iostream>

int main(int argc, char const *argv[])
{
    float FavoriteNumber = 0;
    std::cout<<std::endl << "What's Your Favorite Number; ";
    std::cin >> FavoriteNumber;
    std::cout<<FavoriteNumber<<", That's My Favorite Number Too..."<<std::endl;
    std::cout<<"No Really!, "<<FavoriteNumber<<" Is My Favorite Number :)"<<std::endl;

    return 0;
}
