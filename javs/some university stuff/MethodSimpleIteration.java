package part2;

import Pair.Pair;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

import static utilits.Utilits.*;

public class MethodSimpleIteration {

    private static boolean checkCondition(ArrayList<Double> xk, ArrayList<Double> xk1) {
        for (int i = 0; i < xk.size(); i++) {
            if (Math.abs(xk.get(i) - xk1.get(i)) >= EPSILON) {
                return false;
            }
        }
        return true;
    }

    public static Pair<ArrayList<Double>, Integer> methodSimpleIteration(ArrayList<ArrayList<Double>> A,
                                                                         ArrayList<Double> b) {
        ArrayList<Double> x = new ArrayList<>(Collections.nCopies(A.size(), 1.0));
        ArrayList<Double> xk = new ArrayList<>();
        boolean flag = true;
        int countIteration = 0;
        while (flag) {
            for (int i = 0; i < A.size(); i++) {
                double tmpFrom1ToI = 0.0, tmpFromI1ToN = 0.0;
                for (int j = 0; j < i; j++) {
                    tmpFrom1ToI += A.get(i).get(j) * x.get(j);
                }
                for (int j = i + 1; j < A.size(); j++) {
                    tmpFromI1ToN += A.get(i).get(j) * x.get(j);
                }
                xk.add(1.0 / A.get(i).get(i) * (- tmpFrom1ToI - tmpFromI1ToN + b.get(i)));
            }
            flag = !checkCondition(x, xk);
            Collections.copy(x, xk);
            xk.clear();
            countIteration++;
        }
        return new Pair<>(x, countIteration);
    }

    public static void main(String[] args) {
        System.out.println("2.4 МЕТОД ПРОСТЫХ ИТЕРАЦИЙ");
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите n: ");
        int n  = scanner.nextInt();
        System.out.println("Матрица А");
        ArrayList<ArrayList<Double>> matrA = getMatrAVariant(n);
        //System.out.println(matrA);
        for (ArrayList<Double> ar : matrA) {
            System.out.println(ar);
        }
        System.out.print("X, которые должны получиться: ");
        ArrayList<Double> str = getStrVariant(n);
        System.out.println(str);
        System.out.print("Столбец b: ");
        ArrayList<Double> b = multMatrColumn(matrA, str);
        System.out.println(b);
        Pair<ArrayList<Double>, Integer> method = methodSimpleIteration(matrA, b);
        System.out.print("Найденные методом простых итераций x: ");
        System.out.println(method.getFirst());
        System.out.print("Количество итераций: ");
        System.out.println(method.getSecond());
        System.out.println("Погрешность" + EPSILON);
        System.out.println();
    }
}