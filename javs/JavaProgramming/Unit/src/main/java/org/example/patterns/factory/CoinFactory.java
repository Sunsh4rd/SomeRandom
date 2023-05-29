package org.example.patterns.factory;

public class CoinFactory {
    public static Coin getCoin(String coinType) {
        switch (coinType) {
            case "Gold" -> {
                return new GoldCoin();
            }
            case "Copper" -> {
                return new CopperCoin();
            }
            default -> {
                return null;
            }
        }
    }
}
