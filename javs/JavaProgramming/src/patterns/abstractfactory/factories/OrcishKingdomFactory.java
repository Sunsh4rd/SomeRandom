package patterns.abstractfactory.factories;

import patterns.abstractfactory.components.Army;
import patterns.abstractfactory.components.Castle;
import patterns.abstractfactory.components.King;
import patterns.abstractfactory.orcs.OrcishArmy;
import patterns.abstractfactory.orcs.OrcishCastle;
import patterns.abstractfactory.orcs.OrcishKing;

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
