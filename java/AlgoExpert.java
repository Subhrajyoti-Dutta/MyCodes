import java.util.*;

public class AlgoExpert {
    public static boolean isValidSubsequence(List<Integer> arr, List<Integer> seq) {
        // Write your code here.
        int len_arr=arr.size();
        int len_seq=seq.size();
        int i = 0;
        for (int j=0; j<len_arr; j++){
            if (arr.get(j) == seq.get(i)){
                i+=1;
                if (i==len_seq){
                    return true;
                }
            }
        }
        return false;
    }
    public static void main(String[] args) {
        
    }
}

