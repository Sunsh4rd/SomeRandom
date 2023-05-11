import java.util.Scanner;

public class Task1 {
    public static void main(String[] args) {
//        "Мобайл"
//        Scanner scanner = new Scanner(System.in);
//        int a = scanner.nextInt();
//        int b = scanner.nextInt();
////        int c = scanner.nextInt();
////        int d = scanner.nextInt();
//        System.out.println(a + b);

//        "Рулет"
//        Scanner scanner = new Scanner(System.in);
//        int n = scanner.nextInt();
//        if (n == 1) {
//            System.out.println(0);
//        }
//        else {
//            int it = 0, p = 0;
//            while (n > 0) {
//                it++;
//                p += n % 2;
//                n /= 2;
//            }
//            if (p == 1)
//                System.out.println(--it);
//            else
//                System.out.println(it);
//        }

        Scanner scanner = new Scanner(System.in);
        int a = scanner.nextInt();
        int b = scanner.nextInt();
        int c = scanner.nextInt();
        int d = scanner.nextInt();
        int[] numbers = {a, b, c, d};
        boolean asc = true;
        boolean desc = true;
        //2 1 3 4
        for (int i = 0; i < numbers.length - 1; i++) {
            if (!(numbers[i] >= numbers[i + 1])) {
                desc = false;
                break;
            }
        }
        for (int i = 0; i < numbers.length - 1; i++) {
            if (!(numbers[i] <= numbers[i + 1])) {
                asc = false;
                break;
            }
        }
        if (asc || desc) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
        scanner.close();
    }
}
