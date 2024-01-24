public class InsertionSort {
    static int[] sort(int arr[]){
        int len = arr.length;
        for (int i = 1; i < len; i++){
            int j = i - 1;
            int key = arr[i];
            while (j>=0 && key < arr[j]){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1]=key;
        }
        return arr;
    }
}

class function{
    static void printarr(int arr[]){
        int len = arr.length;
        for (int i = 1; i < len; i++){
            System.out.print(arr[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
}

class Program{
    public static void main(String[] args) {
        int a[] = {110,93,94,91,89,99};
        int sorted_a[] = InsertionSort.sort(a.clone());
        function.printarr(a);
        function.printarr(sorted_a);
    }
}