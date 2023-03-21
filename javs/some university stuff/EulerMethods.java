package part3;

import java.util.ArrayList;

import static utilits.Utilits.*;

public class EulerMethods {
    public static final double h = 1.0;
    public static final int variant = 7; 

    public static double f(double x, double y) {
        return 2 * variant * x + variant * x * x - y;
    }

    public static ArrayList<Double> getYTochonoe(double x0, int n) {
        ArrayList<Double>  y = new ArrayList<>();
        y.add(variant * x0 * x0);
        double xk = x0;
        for (int i = 2; i <= n; i++) {
            xk += h;
            y.add(variant * xk * xk);
        }
        return y;
    }


    public static ArrayList<Double> methodEuler(double x0, double y0, int n) {
        ArrayList<Double>  y = new ArrayList<>();
        y.add(y0);
        double xk = x0;
        for (int i = 1; i < n; i++) {
            double yk = y.get(i - 1);
            y.add(yk + h * f(xk, yk));
            xk += h;
        }
        return y;
    }

    public static ArrayList<Double> upgradeMethodEuler(double x0, double y0, int n) {
        ArrayList<Double>  y = new ArrayList<>();
        y.add(y0);
        double xk = x0;
        for (int i = 1; i < n; i++) {
            double yk = y.get(i - 1);
            y.add(yk + h * f(xk + h / 2.0, yk + h / 2.0 * f(xk, yk)));
            xk += h;
        }
        return y;
    }

    public static ArrayList<Double> methodPreditorCorrector(double x0, double y0, int n) {
        ArrayList<Double>  y = new ArrayList<>();
        y.add(y0);
        double xk = x0;
        for (int i = 1; i < n; i++) {
            double yk = y.get(i - 1);
            y.add(yk + h / 2.0 * (f(xk, yk) + f(xk + h, yk + h * f(xk, yk))));
            xk += h;
        }
        return y;
    }

    public static void main(String[] args) {
        System.out.println("3.1 Метод Эйлера решения задачи Коши для ОДУ первого порядка");
        ArrayList<Double> x = getXWithH(1.0, 10, h);
        ArrayList<Double> yt = getYTochonoe(1.0, 10);
        ArrayList<Double> y1 = methodEuler(1.0, 4.0, 10);
        ArrayList<Double> y2 = upgradeMethodEuler(1.0, 4.0, 10);
        ArrayList<Double> y3 = methodPreditorCorrector(1.0, 4.0, 10);
        System.out.println("Классический метод Эйлера");
        getTable(x, yt, y1);
        System.out.println("Улучшенный метод Эйлера");
        getTable(x, yt, y2);
        System.out.println("Метод предитора-корректора");
        getTable(x, yt, y3);
    }
}
