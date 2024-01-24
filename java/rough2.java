import java.util.*;

public class rough2 {
    static int func( int n, int[] arr, int m) {
        if (n == 0) {
            return 1;
        }
        if (arr[n] != -1) {
            return arr[n];
        }
        int c = 0;
        for (int i = 1; i <= m; i++) {
            if (n - i >= 0) {
                c += func(n - i,arr, m);
            }
        }
        arr[n] = c;
        return arr[n];
    }
    public static void main(String[] args){
        /*Start Your Code Here*/
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        int[] res = new int[T];
        for (int t = 0; t < T; t++) {
            int n = scanner.nextInt();
            int m = scanner.nextInt();
            int[] dp = new int[n + 1];
            Arrays.fill(dp, -1);
            res[t] = func(dp, n, m);
        }
        for (int i = 0; i < T; i++) {
            System.out.println(res[i]);
        }
    }
}