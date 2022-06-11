public class TowerOfHanoi {
    
    public void towerOfHanoi(int n, char from_rod , char to_rod , char using_rod){
        if (n == 0){
            return;
        }
        towerOfHanoi(n-1, from_rod, using_rod,to_rod);
        System.out.println("Move disk "+n+" from "+from_rod+" to "+to_rod);
        towerOfHanoi(n-1, using_rod, to_rod, from_rod);
    }

    public static void main(String[] args){
        int numberOfDisk = 3;
        char from_rod = 'A', using_rod = 'B', to_rod = 'C';

        TowerOfHanoi th = new TowerOfHanoi();
        th.towerOfHanoi(numberOfDisk, from_rod,  to_rod,using_rod);
    }
}
