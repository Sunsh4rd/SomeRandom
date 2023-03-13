package patterns.bridge;

public class Sword implements Weapon {
    private final Enhancement enhancement;

    public Sword(Enhancement enhancement) {
        this.enhancement = enhancement;
    }

    @Override
    public void wield() {
        System.out.println("The sword is wielded.");
        enhancement.onActivate();
    }

    @Override
    public void swing() {
        System.out.println("The sword is swung.");
        enhancement.apply();
    }

    @Override
    public void unwield() {
        System.out.println("The sword is unwielded");
        enhancement.onDeactivate();
    }

    @Override
    public Enhancement getEnhancement() {
        return enhancement;
    }
}
