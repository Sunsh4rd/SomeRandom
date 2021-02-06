package Pair;

import java.util.ArrayList;
import java.util.Objects;

public class Pair<A, B> {
    private A first;
    private B second;

    public Pair() {}

    public Pair(A first, B second) {
        this.first = first;
        this.second = second;
    }

    public String toString() {
        return "(" + first + ", " + second + ")";
    }

    public A getFirst() {
        return first;
    }

    public void setFirst(A first) {
        this.first = first;
    }

    public B getSecond() {
        return second;
    }

    public void setSecond(B second) {
        this.second = second;
    }

    public static ArrayList<Double> getFirstsFromArrayList(ArrayList<Pair<Double, Double>> a) {
        ArrayList<Double> res = new ArrayList<>();
        for (Pair<Double, Double> p : a) {
            res.add(p.getFirst());
        }
        return res;
    }

    public static double findY(ArrayList<Pair<Double, Double>> a, double x) {
        ArrayList<Double> res = new ArrayList<>();
        for (Pair<Double, Double> p : a) {
            if (p.getFirst() == x) {
                return p.getSecond();
            }
        }
        return 0.0;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Pair<?, ?> pair = (Pair<?, ?>) o;
        return Objects.equals(first, pair.first) &&
                Objects.equals(second, pair.second);
    }

    @Override
    public int hashCode() {
        return Objects.hash(first, second);
    }
}