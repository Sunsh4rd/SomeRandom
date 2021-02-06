package utilits;

import Pair.Pair;

import java.util.ArrayList;
import java.util.Scanner;

public class Utilits {

    public static final double EPSILON = 0.0001;
    public static double variant = 4.0;

    public static ArrayList<Pair<Double, Double>> readF() {
        //считали узловые точки и значение в них
        Scanner scanner = new Scanner(System.in);
        System.out.println("Количество узлов: ");
        int n = scanner.nextInt();
        ArrayList<Pair<Double, Double>> f = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            System.out.print("Узел " + i + ": ");
            f.add(new Pair<>(scanner.nextDouble(), scanner.nextDouble()));
        }
        return f;
    }

    public static void printF(ArrayList<Pair<Double, Double>> f) {
        System.out.println("Введенные данные: ");
        for (int i = 0; i < f.size(); i++) {
            System.out.println("x" + i + " = " + f.get(i).getFirst() + " f(x" + i + ") = " + f.get(i).getSecond());
        }
    }

    public static ArrayList<Double> getNewX(ArrayList<Pair<Double, Double>> f) {
        //создали массив, состоящих из узловых точек и точек между ними
        ArrayList<Double> newXs = new ArrayList<>();
        int j = 0;
        for (int i = 0; i < 2 * f.size() - 1; i++) {
            if (i % 2 == 0) {
                newXs.add(f.get(j).getFirst());
                j++;
            } else {
                newXs.add((f.get(j).getFirst() + f.get(j - 1).getFirst()) / 2.0);
            }
        }
        return newXs;
    }

    public static ArrayList<ArrayList<Double>> getTransponirMatr(ArrayList<ArrayList<Double>> matr) {
        ArrayList<ArrayList<Double>> obr = new ArrayList<>();
        for (int i = 0; i < matr.size(); i++) {
            obr.add(new ArrayList<>());
            for (ArrayList<Double> doubles : matr) {
                obr.get(i).add(doubles.get(i));
            }
        }
        return obr;
    }

    public static ArrayList<Double> multMatrColumn(ArrayList<ArrayList<Double>> matrA, ArrayList<Double> str) {
        ArrayList<Double> b = new ArrayList<>();
        int n = matrA.size();

        for (int i = 0; i < n; i++) {
            double tmpSum = 0;
            for (int j = 0; j < n; j++) {
                tmpSum += matrA.get(i).get(j) * str.get(j);
            }
            b.add(tmpSum);
        }

        return b;
    }

    public static ArrayList<ArrayList<Double>> multMatrMatr(ArrayList<ArrayList<Double>> matrA, ArrayList<ArrayList<Double>> matrB) {
        ArrayList<ArrayList<Double>> b = new ArrayList<>();
        int n = matrA.size();

        for (int i = 0; i < n; i++) {
            b.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                double tmpSum = 0;
                for (int k = 0; k < n; k++) {
                    tmpSum += matrA.get(i).get(k) * matrB.get(k).get(j);
                }
                b.get(i).add(tmpSum);
            }
        }
        return b;
    }

    public static ArrayList<ArrayList<Double>> make0(ArrayList<ArrayList<Double>> matr) {
        for (int i = 0; i < matr.size(); i++) {
            for (int j = 0; j < matr.size(); j++) {
                if (matr.get(i).get(j) < EPSILON) {
                    matr.get(i).set(j, 0.0);
                }
            }
        }
        return matr;
    }

    public static ArrayList<ArrayList<Double>> getMatrAVariant(int n) {
        ArrayList<ArrayList<Double>> matr = new ArrayList<>();
        double var = variant;
        for (int i = 0; i < n; i++) {
            matr.add(new ArrayList<>());
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    matr.get(i).add(var);
                } else {
                    matr.get(i).add(var / 100.0);
                }
            }
            var++;
        }
        return matr;
    }

    public static ArrayList<Double> getStrVariant(int n) {
        ArrayList<Double> str = new ArrayList<>();
        double var = variant;
        for (int i = 0; i < n; i++) {
            str.add(var);
            var++;
        }
        return str;
    }

    public static ArrayList<Double> getMatrB(int n) {
        ArrayList<ArrayList<Double>> matrA = getMatrAVariant(n);
        ArrayList<Double> str = getStrVariant(n);
        ArrayList<Double> b = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            double tmpSum = 0;
            for (int j = 0; j < n; j++) {
                tmpSum += matrA.get(i).get(j) * str.get(j);
            }
            b.add(tmpSum);
        }

        return b;
    }

    public static ArrayList<ArrayList<Double>> getMatrAb(ArrayList<ArrayList<Double>> A, ArrayList<Double> b) {
        ArrayList<ArrayList<Double>> matrAb = new ArrayList<>();
        for (int i = 0; i < A.size(); i++) {
            matrAb.add(new ArrayList<>());
            for (int j = 0; j < A.size(); j++) {
                matrAb.get(i).add(A.get(i).get(j));
            }
            matrAb.get(i).add(b.get(i));
        }
        return matrAb;
    }

    public static ArrayList<Double> getXWithH(double x0, int n, double h) {
        ArrayList<Double> x = new ArrayList<>();
        double xk = x0;
        for (int i = 1; i <= n; i++) {
            x.add(xk);
            xk += h;
        }
        return x;
    }

    public static ArrayList<Double> getE(ArrayList<Double> yt, ArrayList<Double> y) {
        ArrayList<Double> e = new ArrayList<>();
        for (int i = 0; i < yt.size(); i++) {
            e.add(Math.abs(yt.get(i) - y.get(i)));
        }
        return e;
    }

    public static void getTable(ArrayList<Double> x, ArrayList<Double> yt, ArrayList<Double> y) {
        System.out.print("x:     ");
        for (double xs : x) {
            System.out.format("%10.5f", xs);
        }
        System.out.println();
        System.out.print("y мет: ");
        for (double ys : y) {
            System.out.format("%10.5f", ys);
        }
        System.out.println();
        System.out.print("y точн:");
        for (double ys : yt) {
            System.out.format("%10.5f", ys);
        }
        System.out.println();
        System.out.print("e:     ");
        ArrayList<Double> e = getE(yt, y);
        for (double es : e) {
            System.out.format("%10.5f", es);
        }
        System.out.println();
        System.out.println();
    }
}