package patterns.abstractfactory.orcs;

import patterns.abstractfactory.components.Army;

public class OrcishArmy implements Army {
    static final String DESCRIPTION = "This is the orcish Army!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
