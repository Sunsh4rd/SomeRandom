import java.util.Scanner;

public class Task2 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        String[] numbers = input.split(" ");

        int n = Integer.parseInt(numbers[0]);
        int m = Integer.parseInt(numbers[1]);
        int k = Integer.parseInt(numbers[2]);

        float result =(float) (n * k) / m;
        int b = (int) result;

        if (result % 1 == 0){
            System.out.println(b);
        }
        else {
            System.out.println(b + 1);
        }
    }
}
