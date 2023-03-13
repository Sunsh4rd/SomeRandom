package patterns.abstractfactory.orcs;

import patterns.abstractfactory.components.King;

public class OrcishKing implements King {
    static final String DESCRIPTION = "This is the orcish King!";

    @Override
    public String getDescription() {
        return DESCRIPTION;
    }
}
