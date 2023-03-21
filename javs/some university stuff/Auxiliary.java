package aux;

import java.util.Scanner;

public class Auxiliary {

	private static final int auxConst = 10;

	public static int addArg(int arg) {
		return arg + auxConst;
	}

	public static int[] allocateArray(int n) {
		return new int[n];
	}

	public static void fillArray(int[] array) {
		Scanner in = new Scanner(System.in);
		for (int i = 0; i < array.length; i++) {
			array[i] = in.nextInt();
		}
	}

	public static void printArray(int[] array) {
		for (int i = 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	}
}