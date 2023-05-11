import java.util.HashMap;
import java.util.Scanner;

public class Task3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int length = scanner.nextInt();
        String input = scanner.next();

        int start = 0;
        int substr_start = -1;
        int min_length = Integer.MAX_VALUE;
        int count = 0;

        HashMap<Character, Integer> charCount = new HashMap<>();
        charCount.put('a', 0);
        charCount.put('b', 0);
        charCount.put('c', 0);
        charCount.put('d', 0);
        for (int j = 0; j < length; j++) {
            int c = charCount.get(input.charAt(j));
            charCount.put(input.charAt(j), ++c);

            if (charCount.get(input.charAt(j)) == 1) {
                count++;
            }

            if (count == 4) {
                while (charCount.get(input.charAt(start)) > 1) {
                    int cc = charCount.get(input.charAt(start));
                    charCount.put(input.charAt(start), --cc);
                    start++;
                }

                int window_length = j - start + 1;
                if (min_length > window_length) {
                    min_length = window_length;
                    substr_start = start;
                }
            }
        }
        if (substr_start == -1) {
            System.out.println(substr_start);
        }
        else {
            System.out.println(input.substring(substr_start, substr_start + min_length).length());
        }
    }
}
