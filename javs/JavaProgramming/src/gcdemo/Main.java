package gcdemo;

import java.util.Random;

public class Main {
    public static void main(String[] args) throws InterruptedException {
//        int size = 1000000;
//        GCMe[] gcmes = new GCMe[size];
//
//        int count = 0;
//        Random rnd = new Random();
//        while (true) {
//            gcmes[rnd.nextInt(size)] = new GCMe();
//            if (count % 1000000 == 0) {
//                System.out.print(".");
//            }
//            count++;
//            Thread.sleep(1);
        String s = "a";
        int count = 1;
        while (true) {
            for (int i = 0; i < count; i++) {
                s += "a";
            }
            count++;
            System.out.println(s);
        }
    }
}

class GCMe {
    long a;
    long aa;
    long aaa;
    long aaaa;
    long aaaaa;
    long aaaaaa;
    long aaaaaaa;
    long aaaaaaaa;
    long aaaaaaaaa;
    long aaaaaaaaaa;
    long aaaaaaaaaaa;
    long aaaaaaaaaaaa;
    long aaaaaaaaaaaaa;
    long aaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaaaaaa;
    long aaaaaaaaaaaaaaaaaaaaaaaaaaaa;
}