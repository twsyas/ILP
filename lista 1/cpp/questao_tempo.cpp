#include <iostream>
using namespace std;
int main(){
    int A, B, C, D, E, F, S;
    int L, Di, Al, K, Fi, Be, V;
    cin>>A>>B>>C>>D>>E>>F;
    L = 2 * abs(A-2023);
    Di = 2 * abs(B-2023);
    Al = 2 * abs(C-2023);
    K = 2 * abs(D-2023);
    Be = 2 * abs(E-2023);
    V =  2 * abs(F-2023);
    S = (L+ Di + Al + K + Be + V);
    cout << "Luther " << L << "\n" << "Diego " << Di << "\n" << "Alisson " << Al << "\n" << "Klaus " << K << "\n" << "Five " << S << "\n" << "Ben " << Be << "\n" << "Viktor " << V << endl;
}