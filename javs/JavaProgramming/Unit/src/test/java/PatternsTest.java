import org.example.patterns.abstractfactory.Kingdom;
import org.example.patterns.abstractfactory.Main;
import org.example.patterns.abstractfactory.orcs.OrcishArmy;
import org.example.patterns.abstractfactory.orcs.OrcishCastle;
import org.example.patterns.abstractfactory.orcs.OrcishKing;
import org.example.patterns.factory.CoinFactory;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class PatternsTest {

    @Test
    public void abstractFactory_throwsIllegalArgumentException() {
        assertThrows(IllegalArgumentException.class, () -> {
            var kingdom = new Kingdom();
            kingdom.createKingdom(Main.FactoryMaker.makeFactory(Main.FactoryMaker.KingdomType.HUMAN));
        });
    }

    @Test
    public void abstractFactory_returnsOrcishKingdom() {
        Kingdom kingdom = new Kingdom();
        kingdom.createKingdom(Main.FactoryMaker.makeFactory(Main.FactoryMaker.KingdomType.ORC));
        assertInstanceOf(OrcishArmy.class, kingdom.getArmy());
        assertInstanceOf(OrcishCastle.class, kingdom.getCastle());
        assertInstanceOf(OrcishKing.class, kingdom.getKing());
    }

    @Test
    public void factory_returnsNull() {
        assertNull(CoinFactory.getCoin("Silver"));
    }
}
