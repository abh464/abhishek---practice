public class PermutationsOfString {
    
    public String swap(String a, int i, int j){ 
        char temp; 
        char[] charArray = a.toCharArray(); 
        temp = charArray[i] ; 
        charArray[i] = charArray[j]; 
        charArray[j] = temp; 
        return String.valueOf(charArray); 
    }

    void permutation(int start, int end, String str){
        if (start == end){
            System.out.println("str: "+str);
            return;
        }

        for (int i = start;i<str.length(); i++){
            str = swap(str,start,i);
            permutation(start+1, end, str);
            str = swap(str,start,i);
        }
    }

    public static void main(String[] args){
        PermutationsOfString ps = new PermutationsOfString();
        String str = "abc";
        ps.permutation(0, str.length(), str);
    }
}
