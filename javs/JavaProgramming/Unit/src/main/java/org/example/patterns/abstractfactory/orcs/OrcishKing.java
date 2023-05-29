package org.example.patterns.abstractfactory.orcs;

import org.example.patterns.abstractfactory.components.King;

public class OrcishKing implements King {
    static final String DESCRIPTION = "This is the orcish King!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
