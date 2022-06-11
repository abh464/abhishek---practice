#include <bits/stdc++.h>
using namespace std;

void printNumber (int n){
    if (n <= 0){
        return;
    }
    cout << "value of n: " << n << "\n";
    printNumber(n-1);
}

int main()
{
    printNumber(5);
    return 0;
}