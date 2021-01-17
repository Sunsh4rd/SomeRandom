package part2;

import Pair.Pair;

import java.util.ArrayList;
import java.util.Scanner;

import static utilits.Utilits.*;

public class MethodProgonki {

    public static ArrayList<ArrayList<Double>> getMatrProgonka4(int n) {
        ArrayList<ArrayList<Double>> res = new ArrayList<>();
        res.add(new ArrayList<>());
        res.get(0).add(variant);
        res.get(0).add(variant / 100.0);
        for (int i = 2; i < n; i++) {
            res.get(0).add(0.0);
        }
        for (int i = 1; i < n - 1; i++) {
            res.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                if (j == i) {
                    res.get(i).add(variant + i);
                } else if (j == i + 1 || j == i - 1) {
                    res.get(i).add((variant + i) / 100.0);
                } else {
                    res.get(i).add(0.0);
                }
            }
        }
        res.add(new ArrayList<>());
        for (int i = 0; i < n - 2; i++) {
            res.get(n - 1).add(0.0);
        }
        res.get(n - 1).add((variant + n - 1) / 100.0);
        res.get(n - 1).add(variant + n - 1);
        return res;
    }

    public static Pair<ArrayList<Double>, ArrayList<Double>> pryamayaProgonka(ArrayList<ArrayList<Double>> diag3,
                                        ArrayList<Double> d) {
        ArrayList<ArrayList<Double>> diag2 = new ArrayList<>();
        ArrayList<Double> p = new ArrayList<>();
        ArrayList<Double> q = new ArrayList<>();
        p.add(null);
        q.add(null);
        p.add(- diag3.get(0).get(1) / diag3.get(0).get(0));
        q.add(d.get(0) / diag3.get(0).get(0));
        for (int i = 1; i < diag3.size() - 1; i++) {
            p.add(diag3.get(i).get(i + 1)
                    / (- diag3.get(i).get(i) - diag3.get(i).get(i - 1) * p.get(i)));
            q.add((diag3.get(i).get(i - 1) * q.get(i)- d.get(i))
                    / (- diag3.get(i).get(i) - diag3.get(i).get(i - 1) * p.get(i)));
        }
        int n = diag3.size() - 1;
        p.add(0.0);
        q.add((diag3.get(n).get(n - 1) * q.get(n)- d.get(n))
                / (- diag3.get(n).get(n) - diag3.get(n).get(n - 1) * p.get(n)));
        return new Pair<>(p, q);
    }

    public static ArrayList<Double> methodProgonki(ArrayList<ArrayList<Double>> diag3,
                                                   ArrayList<Double> d) {
        Pair<ArrayList<Double>, ArrayList<Double>> prog = pryamayaProgonka(diag3, d);
        ArrayList<Double> p = prog.getFirst();
        ArrayList<Double> q = prog.getSecond();
        ArrayList<Double> x = new ArrayList<>();
        int n = diag3.size();
        for (int i = 0; i < n; i++) {
            x.add(0.0);
        }
        x.set(n - 1, q.get(n));
        for (int i = n - 2; i >= 0; i--) {
            x.set(i, p.get(i + 1) * x.get(i + 1) + q.get(i + 1));
        }
        return x;
    }

    public static void main(String[] args) {
        System.out.println("2.3 МЕТОД ПРОГОНКИ");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите n: ");
        int n  = scanner.nextInt();
        System.out.println("Матрица А");
        ArrayList<ArrayList<Double>> matrA = getMatrProgonka4(n);
        //System.out.println(matrA);
        for (ArrayList<Double> ar : matrA) {
            System.out.println(ar);
        }
        System.out.println("X, которые должны получиться");
        ArrayList<Double> str = getStrVariant(n);
        System.out.println(str);
        System.out.println("Столбец d");
        ArrayList<Double> d = multMatrColumn(matrA, str);
        System.out.println(d);
        System.out.println("P и Q");
        Pair<ArrayList<Double>, ArrayList<Double>> pryamProg = pryamayaProgonka(matrA, d);
        System.out.println(pryamProg.getFirst());
        System.out.println(pryamProg.getSecond());
        System.out.println("Результат метода прогонки");
        System.out.println(methodProgonki(matrA, d));
        System.out.println();
    }
}