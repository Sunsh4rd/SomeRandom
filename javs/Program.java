package prog;

import java.util.Scanner;
import static aux.Auxiliary.*;

public class Program {
	
	public static void main(String[] args) {
		
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		System.out.println(addArg(number));
	}
}