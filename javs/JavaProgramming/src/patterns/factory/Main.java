package patterns.factory;

public class Main {
    public static void main(String[] args) {

        var goldCoin = CoinFactory.getCoin("Gold");
        var copperCoin = CoinFactory.getCoin("Copper");

        goldCoin.getDescription();
        copperCoin.getDescription();
    }
}
