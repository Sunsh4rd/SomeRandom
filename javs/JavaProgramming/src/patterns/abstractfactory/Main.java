package patterns.abstractfactory;

import patterns.abstractfactory.factories.ElvenKingdomFactory;
import patterns.abstractfactory.factories.KingdomFactory;
import patterns.abstractfactory.factories.OrcishKingdomFactory;

public class Main {
    private static class FactoryMaker {
        private enum KingdomType {
            ELF, ORC
        }

        public static KingdomFactory makeFactory(KingdomType type) {
            switch (type) {
                case ELF -> {
                    return new ElvenKingdomFactory();
                }
                case ORC -> {
                    return new OrcishKingdomFactory();
                }
                default -> throw new IllegalArgumentException("KingdomType not supported.");
            }
        }
    }

    public static void main(String[] args) {
        var kingdom = new Kingdom();
        kingdom.createKingdom(FactoryMaker.makeFactory(FactoryMaker.KingdomType.ELF));
        System.out.println(kingdom);
        kingdom.createKingdom(FactoryMaker.makeFactory(FactoryMaker.KingdomType.ORC));
        System.out.println(kingdom);
    }
}
