#include <bits/stdc++.h>
using namespace std;

void permutation(int start, int end, string str){
    if (start == end){
        cout << "str: " << str << "\n";
        return;
    }

    for (int i = start; i < end; i++) { 
        swap(str[start], str[i]); 
        permutation(start+1, end, str); 
        swap(str[start], str[i]); 
    }
}

int main()
{
    string str = "abc";
    permutation(0,str.length(),str);
    return 0;
}