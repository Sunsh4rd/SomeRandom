package org.example.patterns.abstractfactory.factories;

import org.example.patterns.abstractfactory.components.Army;
import org.example.patterns.abstractfactory.components.Castle;
import org.example.patterns.abstractfactory.components.King;
import org.example.patterns.abstractfactory.orcs.OrcishArmy;
import org.example.patterns.abstractfactory.orcs.OrcishCastle;
import org.example.patterns.abstractfactory.orcs.OrcishKing;

public class OrcishKingdomFactory implements KingdomFactory {
    @Override
    public Castle createCastle() {
        return new OrcishCastle();
    }

    @Override
    public King createKing() {
        return new OrcishKing();
    }

    @Override
    public Army createArmy() {
        return new OrcishArmy();
    }
}
