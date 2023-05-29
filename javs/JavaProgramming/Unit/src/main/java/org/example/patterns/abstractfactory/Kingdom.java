package org.example.patterns.abstractfactory;

import org.example.patterns.abstractfactory.components.Army;
import org.example.patterns.abstractfactory.components.Castle;
import org.example.patterns.abstractfactory.components.King;
import org.example.patterns.abstractfactory.factories.KingdomFactory;

public class Kingdom {
    private Army army;
    private Castle castle;
    private King king;

    public Kingdom() {
    }

    public void createKingdom(KingdomFactory factory) {
        this.army = factory.createArmy();
        this.castle = factory.createCastle();
        this.king = factory.createKing();
    }

    public Army getArmy() {
        return army;
    }

    public Castle getCastle() {
        return castle;
    }

    public King getKing() {
        return king;
    }

    @Override
    public String toString() {
        return String.format("%s %s %s", army.getDescription(), castle.getDescription(), king.getDescription());
    }
}
