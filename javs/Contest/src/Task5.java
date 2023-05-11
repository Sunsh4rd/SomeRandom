import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class Task5 {

    public static boolean isSensible(int[] section, int i, int j) {
        int sum = 0;
        for (int k = i; k < j; k++) {
            sum += section[k];
        }
        return sum == 0;
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.useDelimiter("\n");
        int length = scanner.nextInt();
        List<Integer> numbers = Arrays.stream(scanner.next().split(" ")).map(Integer::parseInt).toList();
        System.out.println(length);
        System.out.println(numbers);
        for (int i = 0; i < numbers.size(); i++) {

        }
    }
}
