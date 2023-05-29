package org.example.patterns.factory;

public class Main {
    public static void main(String[] args) {

        var goldCoin = CoinFactory.getCoin("Gold");
        var copperCoin = CoinFactory.getCoin("Copper");
        var silverCoin = CoinFactory.getCoin("Silver");

        if (goldCoin != null) {
            goldCoin.getDescription();
        }
        else {
            throw new NullPointerException();
        }
        if (copperCoin != null) {
            copperCoin.getDescription();
        }
        else {
            throw new NullPointerException();
        }
        if (silverCoin != null) {
            silverCoin.getDescription();
        }
        else {
            throw new NullPointerException();
        }
    }
}
