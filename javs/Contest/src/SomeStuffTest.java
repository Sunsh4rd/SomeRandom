import java.util.HashMap;
import java.util.Map;

public class SomeStuffTest {
    public static void main(String[] args) {

        Map<Base, Integer> someMap = new HashMap<Base, Integer>();

        var base1 = new Base(new StringBuilder("state1"));
        var base2 = new Base(new StringBuilder("state2"));
        var base3 = new Base(new StringBuilder("state3"));
        var base4 = new Base(new StringBuilder("state4"));

        someMap.put(base1, 1);
        someMap.put(base2, 2);
        someMap.put(base3, 3);
        someMap.put(base4, 4);
        System.out.println(someMap);

        base1.setState(new StringBuilder("state0"));

        System.out.println(someMap);
    }
}

class Base {

    private StringBuilder state;

    public Base(StringBuilder state) {
        this.state = state;
    }

    public StringBuilder getState() {
        return state;
    }

    public void setState(StringBuilder state) {
        this.state = state;
    }

    private void someMethod() {
        System.out.println("private");
    }

    public void publicMethod() {
        someMethod();
    }
}

//class Child extends Base {
//
//}