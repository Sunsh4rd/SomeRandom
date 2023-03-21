package patterns.command;

public abstract class Target {

    protected enum Size {
        SMALL, NORMAL
    }

    protected enum Visibility {
        VISIBLE, INVISIBLE
    }
    private Size size;

    private Visibility visibility;

    public Size getSize() {
        return size;
    }

    public void setSize(Size size) {
        this.size = size;
    }

    public Visibility getVisibility() {
        return visibility;
    }

    public void setVisibility(Visibility visibility) {
        this.visibility = visibility;
    }

    @Override
    public abstract String toString();

    public void printStatus() {
        System.out.printf("%s, [size=%s] [visibility=%s]%n", this, getSize(), getVisibility());
    }
}
