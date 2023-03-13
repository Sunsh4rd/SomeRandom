package patterns.bridge;

public interface Weapon {
    void wield();
    void swing();
    void unwield();
    Enhancement getEnhancement();
}
