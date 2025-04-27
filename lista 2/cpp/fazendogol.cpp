#include <iostream>
using namespace std;
int main(){
    char z,g,d,c;
    cin>>z>>g;
    cin>>d>>c;

    if (z==d){
        cout<<"Driblado"<<endl;
        if(c == g){
            cout<<"Gol";
        }
        else{
            cout<<"...e o goleiro pega"<<endl;
        }
        
    }
    else{
        cout<<"Bloqueado"<< endl;
        cout<<" ";
    }

}
