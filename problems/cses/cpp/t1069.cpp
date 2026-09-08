#include <bits/stdc++.h>

using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string dna;
    long long resp = 0, maior = 1;

    cin >> dna;

    for(int i = 1; i < dna.length(); i++){
        
        if (dna[i] == dna[i - 1]) maior += 1;
        else {
            if (maior > resp) resp = maior;
            maior = 1;
        }

    }

    if (maior > resp) resp = maior;
    cout << resp << '\n';


}