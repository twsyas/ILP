#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int C, c, X, cubos;
    cin>>C>>c>>X;
    if(C%c != 0){
        cout<< "!Eh possivel";
    }
    else{
        cubos = (cbrt(C/c));
        if(cubos <= X){
            cout<<"Eh possivel";
        }
        else{
            cout<<"!Eh possivel";
        }
    }
}

// refazer