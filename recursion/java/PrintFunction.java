public class PrintFunction {

    public void printNumber(int n){
        if (n <= 0){
            return;
        }
        System.out.println("value of n: "+n);
        printNumber(n-1);
    }

    public static void main(String[] args) {
        PrintFunction pf = new PrintFunction();
        pf.printNumber(5);
    }
}