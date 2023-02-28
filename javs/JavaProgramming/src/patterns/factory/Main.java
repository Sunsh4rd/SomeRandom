package patterns.factory;

public class Main {
    public static void main(String[] args) {
        System.out.println("factory");

        var goldCoin = CoinFactory.getCoin("Gold");
        var copperCoin = CoinFactory.getCoin("Copper");

        goldCoin.getDescription();
        copperCoin.getDescription();
    }
}
