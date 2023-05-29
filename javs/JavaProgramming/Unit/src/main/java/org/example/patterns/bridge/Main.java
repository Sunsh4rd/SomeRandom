package org.example.patterns.bridge;

public class Main {
    public static void main(String[] args) {
        System.out.println("Soul eating sword and flying hammer:");
        var enhancedSword = new Sword(new SoulEatingEnhancement());
        enhancedSword.wield();
        enhancedSword.swing();
        enhancedSword.unwield();

        var enhancedHammer = new Hammer(new FlyingEnhancement());
        enhancedHammer.wield();
        enhancedHammer.swing();
        enhancedHammer.unwield();

        System.out.println();

        System.out.println("Soul eating hammer and flying sword:");
        enhancedSword = new Sword(new FlyingEnhancement());
        enhancedSword.wield();
        enhancedSword.swing();
        enhancedSword.unwield();

        enhancedHammer = new Hammer(new SoulEatingEnhancement());
        enhancedHammer.wield();
        enhancedHammer.swing();
        enhancedHammer.unwield();
    }
}
