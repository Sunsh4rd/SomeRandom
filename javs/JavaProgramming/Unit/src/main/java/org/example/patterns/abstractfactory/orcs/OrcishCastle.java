package org.example.patterns.abstractfactory.orcs;

import org.example.patterns.abstractfactory.components.Castle;

public class OrcishCastle implements Castle {
    static final String DESCRIPTION = "This is the orcish castle!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
