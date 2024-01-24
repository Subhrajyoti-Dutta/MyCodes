import java.util.*;

public class floyd_warshall_algo{
    static double inf = Double.POSITIVE_INFINITY;
    public static void main(String[] args){
        double[][] data = {{inf, inf, inf, inf, inf, inf},
                           {  1, inf, inf,   2, inf, inf},
                           { -4,   2, inf,  -1, inf, inf},
                           {inf, inf, inf, inf, inf,  -5},
                           {inf, inf,   4,   7, inf, inf},
                           {inf, inf, inf, inf,   6, inf}};

        Main test = new Main(data);
        test.compute();
        test.print();
    }
}

class Main{
    int n;
    double[][][] A;
    public Main(double[][] A0){
        n = A0.length;
        A = new double[n+1][n][n];
        A[0] = A0;
    }

    public void compute(){
        for (int k = 1; k <= n; k++){
            for (int i = 0; i < n; i++){
                for (int j = 0; j < n; j++){
                    double via = A[k-1][i][k-1] + A[k-1][k-1][j];
                    double direct = A[k-1][i][j];
                    A[k][i][j] = (via < direct)? via : direct;
                }
            }
        }
    }

    public void print (){
        for (int i = 0; i <= n; i++){
            //System.out.print("\nMatrix number: ");
            //System.out.print(i);
            System.out.print("\n[\n");
            for (int j = 0; j < n; j++){
                System.out.print("   ");
                System.out.print(Arrays.toString(A[i][j]));
                System.out.print("\n");
            }
            if (i!=n){ 
                System.out.print("],\n");
            } else {
                System.out.print("]\n");
            }
        }
    }
}