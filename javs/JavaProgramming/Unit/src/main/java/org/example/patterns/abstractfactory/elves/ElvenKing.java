package org.example.patterns.abstractfactory.elves;

import org.example.patterns.abstractfactory.components.King;

public class ElvenKing implements King {
    static final String DESCRIPTION = "This is the elven King!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
