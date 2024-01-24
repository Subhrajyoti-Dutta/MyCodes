import java.util.Scanner;

public class random {
	static int sum( int[] num ) {
		int res = 0;
		int leng = num.length;
		for ( int i = 0; i < leng; i++ ) {
			res += num[i];
		}
		return res;
	}

	public static void main( String[] args ) {
		Scanner input = new Scanner( System.in );
		System.out.print( "Number of Input arrays: " );
		int no_of_array = input.nextInt();
		int[][] list_of_array = new int[no_of_array][];

		for ( int i = 0; i < no_of_array; i++ ) {
			System.out.print( "What is the length of array: " );
			int leng = input.nextInt();
			int[] temp_list = new int[leng];
			System.out.println( "Write the elements of the array:" );
			for ( int j = 0; j < leng; j++ ) {
				temp_list[j] = input.nextInt();
			}
			list_of_array[i] = temp_list;
		}
		for ( int i = 0; i < no_of_array; i++ ) {
			int result = sum( list_of_array[i] );
			System.out.println( result );

        input.close();
		}
	}
}