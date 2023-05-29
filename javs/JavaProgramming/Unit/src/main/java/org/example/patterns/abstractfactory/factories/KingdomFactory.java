package org.example.patterns.abstractfactory.factories;

import org.example.patterns.abstractfactory.components.Army;
import org.example.patterns.abstractfactory.components.Castle;
import org.example.patterns.abstractfactory.components.King;

public interface KingdomFactory {
    Castle createCastle();
    King createKing();
    Army createArmy();
}
