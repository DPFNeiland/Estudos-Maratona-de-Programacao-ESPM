
#include <bits/stdc++.h>

using namespace std;


void CalculoCN(double* Pcompra, double* Pvenda, string* Presp, int n){

    double somaCompra = 0, somaVenda = 0, calculo;

    for(int i = 0; i < n; i++){
        somaCompra += *(Pcompra + i); 
        somaVenda  += *(Pvenda + i);  
        
        calculo = (somaCompra - somaVenda) / (somaCompra + somaVenda);

        if (calculo > 0) *(Presp + i) = "COMPRA";
        if (calculo < 0) *(Presp + i) = "VENDA";
        else *(Presp + i) = "NEUTRO";
    }
}

int main(){

    int n, q;
    double c, v;

    cin >> n;
    double compra[n], venda[n];
    string resp[n];

    for(int i = 0; i < n; i++){
        cin >> c >> v;

        compra[i] = c;
        venda[i] = v;
    }

    CalculoCN(compra, venda, resp, n);
    
    cin >> q;
    for(int i = 0; i < q; i++){
        cin >> n;

        cout << resp[n - 1] << '\n';
    }

}