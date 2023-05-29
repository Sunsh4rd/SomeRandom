package org.example.patterns.factory;

public class CopperCoin implements Coin {
    @Override
    public void getDescription() {
        System.out.println("A not so shiny copper coin.");
    }
}
