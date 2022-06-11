#include <bits/stdc++.h>
using namespace std;
 
void towerOfHanoi(int n, char from_rod, char to_rod, char using_rod){
    if (n == 0){
        return;
    }
    towerOfHanoi(n - 1, from_rod, using_rod, to_rod);
    cout << "Move disk " << n << " from " << from_rod << " to " << to_rod << "\n";
    towerOfHanoi(n - 1, using_rod, to_rod, from_rod);
}
 
int main()
{
    int numberOfDisk = 3;
    char from_rod = 'A', using_rod = 'B', to_rod = 'C'; 
    towerOfHanoi(numberOfDisk, from_rod,  to_rod,using_rod);
    return 0;
}