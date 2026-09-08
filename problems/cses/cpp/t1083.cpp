#include <bits/stdc++.h>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n, soma, aux = 0;

    cin >> n;

    soma = (n + 1LL)*n/2LL;

    for(int i = 0; i < n - 1; i ++){
        cin >> aux;
        soma -= aux;        
    }

    cout << soma << '\n';
}