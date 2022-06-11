#include <bits/stdc++.h>
using namespace std;

int fibonacciSeries(int n){
    if (n<=0){
        return 0;
    }else if (n == 1 || n == 2)
    {
        return 1;
    }
    int previousSum = fibonacciSeries(n-1)+fibonacciSeries(n-2);
    return previousSum;
}

int main()
{
    int n = 6;
    int sum = fibonacciSeries(n);
    cout << "Fibonacci of "<< n << " is : " << sum;
    return 0;
}