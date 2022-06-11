#include <bits/stdc++.h>
using namespace std;

void swap(int *arr,int i, int j){
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int *repeatingMissingNumberBruteForce(int *arr, int arrLength) {
    
    sort(arr,arr+arrLength);

    int *result=new int[2];

    for(int i=0;i<arrLength;i++){
        if (i == arrLength-1){
            break;
        }

        if(arr[i]==arr[i+1]){
            result[0]=arr[i]; 
            break;
        }
    }

    for(int i=0;i<arrLength;i++){
        if (i == arrLength-1){
            break;
        }

        if(arr[i] != i+1){
            result[1]=i+1; 
            break;
        }
    }


    return result;
}

int *repeatingMissingNumberBetter(int *arr, int arrLength) {
    
    int *result=new int[2];
    int countArray[arrLength]={0};

    for(int i=0;i<arrLength;i++){
        countArray[arr[i]-1]+=1;
    }

    for (int i = 0; i < arrLength; ++i){
        if (countArray[i] == 0){
            result[1] = i+1;
        }
        
        if (countArray[i] == 2){
            result[0] = i+1;
        }
    }
      
    return result;
}

int *repeatingMissingNumberOptimized(int *arr, int arrLength) {
    int *result=new int[2];

    int i = 0;
    while (i < arrLength) {
        if (arr[i] == arr[arr[i] - 1]) {
            i++;
        }
        else {
            if (arr[i] != arr[arr[i] - 1]) {
                swap(arr, i, arr[i] - 1);
            }
            else {
                i++;
            }
        }
    }

    for (i = 0; i < arrLength; i++) {
        if (arr[i] != i+1) {
            result[0] = arr[i];
            result[1] = i+1;
            break;
        }
    }

    return result;
}
int main()
{
    int arr[] = { 3, 2, 3 };
    int arrLength = sizeof(arr) / sizeof(arr[0]);

    cout << "\nBrute-force\n";
    int *result = repeatingMissingNumberBruteForce(arr,arrLength);
    for (int i = 0; i<2;i++){
        cout << result[i] <<"\n";
    }
    cout << "Better\n";
    result = repeatingMissingNumberBetter(arr,arrLength);
    for (int i = 0; i<2;i++){
        cout << result[i] <<"\n";
    }
    
    cout << "Optimized\n";
    result = repeatingMissingNumberOptimized(arr,arrLength);
    for (int i = 0; i<2;i++){
        cout << result[i] <<"\n";
    }
    return 0;
}