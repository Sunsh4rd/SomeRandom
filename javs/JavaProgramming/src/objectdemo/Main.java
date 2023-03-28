package objectdemo;

public class Main {

    public static void main(String[] args) {
        var entityWithDefaultToString = new EntityWithDefaultToString(1, "Default");
        var entityWithOverriddenToString = new EntityWithOverriddenToString(2, "Overridden");

        System.out.println(entityWithDefaultToString);
        System.out.println(entityWithOverriddenToString);
    }
}
