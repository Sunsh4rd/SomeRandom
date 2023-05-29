package org.example.patterns.abstractfactory.elves;

import org.example.patterns.abstractfactory.components.Army;

public class ElvenArmy implements Army {
    static final String DESCRIPTION = "This is the elven Army!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
