
#include <iostream>

using namespace std;

int main(){
    double n1, n2, media;

    cout << "Primeira nota: ";
    cin >> n1;
    cout << "Segunda nota: ";
    cin >> n2;

    media = (n1 + n2)/2;
    cout << media << '\n';

    if ( media >=7.0 )
        cout << "aprovado" << '\n';
    else 
        cout << "reprovado" << '\n';


}