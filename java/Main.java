import java.util.*;

public class Main {
    public static int func(int[] arr){
        int totalSum = sum(arr);
        int sum = 0;
        int breakPoint = 0;
        for (int i = 0; i < arr.length; i++) {
            totalSum -= arr[i];
            if (sum == totalSum / 2) {
                breakPoint = i;
                break;
            } else if (sum > totalSum/2) {
                return 0;
            }
        }
        int leftarr[] = new int[breakPoint+1];
        int rightarr[] = new int[arr.length - breakPoint - 1];
        return 1+Math.max(func(leftarr), func(rightarr));
    }

    public static int sum(int[] arr) {
        int res = 0;
        for (int i = 0; i < arr.length; i++) {
            res += arr[i];
        }
        return res;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner( System.in );
        int T = scanner.nextInt();
        for (int t = 0; t < T; t++) {
            int N = scanner.nextInt();
            int[] A = new int[N];
            for (int i = 0; i < N; i++) {
                A[i] = scanner.nextInt();
            }
            System.out.println(func(A));
        }
    }
}