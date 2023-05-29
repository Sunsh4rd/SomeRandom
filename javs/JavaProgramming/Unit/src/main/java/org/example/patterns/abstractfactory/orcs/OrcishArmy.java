package org.example.patterns.abstractfactory.orcs;

import org.example.patterns.abstractfactory.components.Army;

public class OrcishArmy implements Army {
    static final String DESCRIPTION = "This is the orcish Army!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
