package patterns.abstractfactory.factories;

import patterns.abstractfactory.components.Army;
import patterns.abstractfactory.components.Castle;
import patterns.abstractfactory.components.King;

public interface KingdomFactory {
    Castle createCastle();
    King createKing();
    Army createArmy();
}
