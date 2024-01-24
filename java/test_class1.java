import java.util.Scanner;

public class test_class1 {

	static class Student {
		public String name;
		public int math_marks;
		public int phy_marks;
		public int chem_marks;
		protected long reg_no;
		Scanner input = new Scanner( System.in );
		private double average = -1.0;
		public String DOB;

		public void initialize() {
			math_marks = 0;
			phy_marks = 0;
			chem_marks = 0;
			average = -1;
			name = "";
			System.out.print( "Name of the Student: " );
			name = input.next();
			System.out.print( "Registration number: " );
			reg_no = input.nextLong();
			System.out.print( "DOB of the Student: " );
			DOB = input.next();
			math_marks = input_marks( "Math" );
			phy_marks = input_marks( "Physics" );
			chem_marks = input_marks( "Chemistry" );
		}

		private int input_marks( String sub_name ) {
			String str = String.join( "", "Enter the marks for ", sub_name, ": " );
			System.out.print( str );
			return input.nextInt();
		}

		public double avg() {
			if ( average == -1 ) {
                average = ( double ) ( math_marks + phy_marks + chem_marks ) / 3.0;
			}
			return average;
		}

		public void print_name() {
			System.out.println( name );
		}
	}
    public static void main( String[] args ) {
		Student subhrajyoti = new Student();
		subhrajyoti.initialize();
		subhrajyoti.print_name();
		System.out.println( subhrajyoti.avg() );
        System.out.println( subhrajyoti.DOB );
	}
}