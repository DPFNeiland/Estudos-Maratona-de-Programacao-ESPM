#include <bits/stdc++.h>

using namespace std;

void trocar(int*pa, int*pb);

int main(){
    int a, b;
    cout << "informe o primeiro valor: ";
    cin >> a;
    cout << "informe o segundo valor: ";
    cin >> b;
    trocar(&a, &b);
    cout << a << '\n';
    cout << b << '\n';

}

void trocar(int*pa, int*pb){
    int aux;
    aux = *pa;
    *pa = *pb;
    *pb = aux;

}