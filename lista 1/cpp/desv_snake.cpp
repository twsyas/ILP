#include <iostream>
using namespace std;
int main(){
    int Q1, Q2, Q3, total, total_u, E1, E2, E3, resposta;
    cin>>Q1>>Q2>>Q3;
    total = Q1+Q2+Q3;
    cin>>E1>>E2>>E3;
    total_u = (E1*3)+(E2*3)+(E3*3);
    resposta = (total - total_u);
    cout<<resposta;
}