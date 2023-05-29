package org.example.patterns.abstractfactory.factories;

import org.example.patterns.abstractfactory.components.Army;
import org.example.patterns.abstractfactory.components.Castle;
import org.example.patterns.abstractfactory.components.King;
import org.example.patterns.abstractfactory.elves.ElvenArmy;
import org.example.patterns.abstractfactory.elves.ElvenCastle;
import org.example.patterns.abstractfactory.elves.ElvenKing;

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
