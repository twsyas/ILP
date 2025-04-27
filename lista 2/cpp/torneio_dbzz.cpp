#include <iostream>
using namespace std;
int main(){
    int n1, n2, n3, n4, n5, soma;
    cin>>n1>>n2>>n3>>n4>>n5;
    soma =(n1+n2+n3+n4+n5);
    if (soma > 5000){
        cout<<"Acesso proibido";
    }
    else{
        cout<<"Acesso liberado";
    }
}