package org.example.patterns.factory;

public class GoldCoin implements Coin {

    @Override
    public void getDescription() {
        System.out.println("A shiny gold coin.");
    }
}
