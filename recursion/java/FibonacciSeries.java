public class FibonacciSeries {

    public int fibonacciSeries(int n){
        if (n <= 0){
            return 0;
        } else if (n == 1 || n == 2){
            return 1;
        }
        int previousSum = fibonacciSeries(n-1)+fibonacciSeries(n-2);
        return previousSum;
    }
    public static void main(String[] args){
        FibonacciSeries fs = new FibonacciSeries();
        int n = 6;
        int sum = fs.fibonacciSeries(n);
        System.out.println("Fibonacci of "+n+" is : "+sum);
    }
}
