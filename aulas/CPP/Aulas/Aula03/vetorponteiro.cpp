#include <bits/stdc++.h>

using namespace std;

void lerDados(int* p, int n){
    
    for(int i = 0; i < n; i++){
        cout << " valor --> ";
        cin >> *(p + i);

    }   

}

void imprimir(int* p, int n){
    for(int i = 0; i < n; i++){
        cout << *(p + i) << endl;

    }   
}

int main(){
    int n = 5;    
    int v[n];

    lerDados(v, n);
    imprimir(v, n);

}
