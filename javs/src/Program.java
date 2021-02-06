package prog;

import java.util.Scanner;
import static aux.Auxiliary.*;
import pet.Pet;
import cat.Cat;

public class Program {
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int number = in.nextInt();
		int[] array = allocateArray(number);
		fillArray(array);
		printArray(array);

		Pet p = new Pet("UN");
		p.speak();
		Cat c = new Cat("Tom");
		c.speak();
	}
}