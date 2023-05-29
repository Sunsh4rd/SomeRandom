package org.example.patterns.abstractfactory;

import org.example.patterns.abstractfactory.factories.ElvenKingdomFactory;
import org.example.patterns.abstractfactory.factories.KingdomFactory;
import org.example.patterns.abstractfactory.factories.OrcishKingdomFactory;

public class Main {
    public static class FactoryMaker {
        public enum KingdomType {
            ELF, ORC, HUMAN
        }

        public static KingdomFactory makeFactory(KingdomType type) throws IllegalArgumentException {
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
        kingdom.createKingdom(FactoryMaker.makeFactory(FactoryMaker.KingdomType.HUMAN));
        System.out.println(kingdom);
    }
}
