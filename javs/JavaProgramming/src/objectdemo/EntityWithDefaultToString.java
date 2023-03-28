package objectdemo;

import java.util.Objects;

public class EntityWithDefaultToString {

    protected int number;
    protected String name;

    public EntityWithDefaultToString(int number, String name) {
        this.number = number;
        this.name = name;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        EntityWithDefaultToString that = (EntityWithDefaultToString) o;
        return number == that.number && Objects.equals(name, that.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(number, name);
    }
}
