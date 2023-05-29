package org.example.patterns.bridge;

public class Hammer implements Weapon {
    private final Enhancement enhancement;

    public Hammer(Enhancement enhancement) {
        this.enhancement = enhancement;
    }

    @Override
    public void wield() {
        System.out.println("The hammer is wielded.");
        enhancement.onActivate();
    }

    @Override
    public void swing() {
        System.out.println("The hammer is swung.");
        enhancement.apply();
    }

    @Override
    public void unwield() {
        System.out.println("The hammer is unwielded.");
        enhancement.onDeactivate();
    }

    @Override
    public Enhancement getEnhancement() {
        return enhancement;
    }
}
