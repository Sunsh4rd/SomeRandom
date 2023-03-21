package patterns.bridge;

public interface Enhancement {
    void onActivate();
    void apply();
    void onDeactivate();
}
