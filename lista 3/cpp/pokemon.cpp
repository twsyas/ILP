#include <iostream>
using namespace std;
int main(){
    int E, P, td, d;
    td = 0;
    cin >> E>> P;
    while(E>0 and P>0){
        E-=P;
        P -= 1;
        td += 1;
    }
    if (E<=0){
        cout<<td;
    }
    else{
        cout<<"F";
    }

    }