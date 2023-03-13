package patterns.abstractfactory.factories;

import patterns.abstractfactory.components.Army;
import patterns.abstractfactory.components.Castle;
import patterns.abstractfactory.components.King;
import patterns.abstractfactory.elves.ElvenArmy;
import patterns.abstractfactory.elves.ElvenCastle;
import patterns.abstractfactory.elves.ElvenKing;

public class ElvenKingdomFactory implements KingdomFactory {

    @Override
    public Castle createCastle() {
        return new ElvenCastle();
    }

    @Override
    public King createKing() {
        return new ElvenKing();
    }

    @Override
    public Army createArmy() {
        return new ElvenArmy();
    }
}
