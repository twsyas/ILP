#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int X, Y, area, resto;
    cin>>X>>Y;
    area = (X-(9*Y));
    resto = area/9;
    if((resto-area)< 0){
        cout<<"Precisa de mais difusores!";
        cout<<(abs(resto+1));
    }
    else{
        cout<<"Lar doce lar.";
    }
}