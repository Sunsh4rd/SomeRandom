package objectdemo;

public class EntityWithOverriddenToString extends EntityWithDefaultToString {

    public EntityWithOverriddenToString(int number, String name) {
        super(number, name);
    }

    @Override
    public String toString() {
        return String.format("EntityWithOverriddenToString{number=%d, name=%s}", this.number, this.name);
    }

    @Override
    public int hashCode() {
        return super.hashCode();
    }

    @Override
    public boolean equals(Object obj) {
        return super.equals(obj);
    }
}
