package patterns.abstractfactory;

import patterns.abstractfactory.components.Army;
import patterns.abstractfactory.components.Castle;
import patterns.abstractfactory.components.King;
import patterns.abstractfactory.factories.KingdomFactory;

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

    @Override
    public String toString() {
        return String.format("%s %s %s", army.getDescription(), castle.getDescription(), king.getDescription());
    }
}
