import java.util.Arrays;

public class RepeatingMissingNumber {

    static void swap(int[] arr, int a, int b)
    {
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }


    int[] repeatingMissingNumberBruteForce(int arr[]){
        int arrLength = arr.length;
        
        Arrays.sort(arr);
        
        int[] result = new int[2];
        
        for (int i = 0; i < arrLength; ++i){
            if(i == arrLength-1){
                break;
            }
             
            if(arr[i] == arr[i+1]){
                result[0] = arr[i];
                
            }
            
        }

        for (int i = 0; i < arrLength; ++i){
            if(i == arrLength-1){
                break;
            }

            if( arr[i]!= i+1){
                result[1] = i+1;
                break;
            }
        }

        return result;
    }

    int[] repeatingMissingNumberBetter(int arr[]){
        int arrLength = arr.length;
        
        int[] result = new int[2];
        
        int [] countArray = new int[arrLength];
        Arrays.fill(countArray, 0);

        for (int i = 0; i < arrLength; ++i){
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

    int[] repeatingMissingNumberOptimized(int arr[]){
        int arrLength = arr.length;
        
        int[] result = new int[2];
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

    public static void main(String[] args){
        RepeatingMissingNumber rmn = new RepeatingMissingNumber();
        int arr[] = {3,1,3};

        System.out.println("Brute-force");
        for (int n: rmn.repeatingMissingNumberBruteForce(arr)){
            System.out.println(n);
        }

        System.out.println("Better");
        for (int n: rmn.repeatingMissingNumberBetter(arr)){
            System.out.println(n);
        }


        System.out.println("Optimized");
        for (int n: rmn.repeatingMissingNumberOptimized(arr)){
            System.out.println(n);
        }
    }
}
