#include <iostream>
using namespace std;
int main(){
    int SC, MM, CK, finalSC, finalMM,finalCK;
    cin>>SC>>MM>>CK;
    finalSC = (30 - SC);
    finalMM = (6-MM);
    finalCK = (3-CK);

    if(SC < 30){
        cout<< finalSC << " " << finalMM << " " << finalCK;
    }
    else{
        cout<<"PROXIMO MUNDO";
    }
}