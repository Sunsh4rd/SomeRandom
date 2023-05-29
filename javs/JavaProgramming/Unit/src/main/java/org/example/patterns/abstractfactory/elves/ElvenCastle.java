package org.example.patterns.abstractfactory.elves;

import org.example.patterns.abstractfactory.components.Castle;

public class ElvenCastle implements Castle {
    static final String DESCRIPTION = "This is the elven castle!";
    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
