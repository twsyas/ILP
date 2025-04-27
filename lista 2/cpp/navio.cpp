#include <iostream>
using namespace std;
int main(){
    int X, Y;
    cin>>X>>Y;
    if((X <= 0 or X >= 100) | (Y <= 0 or Y >= 100)){
        cout<<"Coordenada invalida";
        
    }
    else{
        if((X>=71 or Y>=71)){
            cout<<"Coordenada valida e o navio esta longe";
        }
        else{
            cout<<"Coordenada valida e o navio esta perto";
        }
    }    
}