package patterns.proxy;

import patterns.factory.Wizard;

public class WizardTowerProxy implements WizardTower {

    private static final int NUMBER_OF_WIZARDS_ALLOWED = 3;

    private int numberOfWizards;

    private final WizardTower tower;

    public WizardTowerProxy(WizardTower tower) {
        this.tower = tower;
    }

    @Override
    public void enter(Wizard wizard) {
        if (numberOfWizards < NUMBER_OF_WIZARDS_ALLOWED) {
            tower.enter(wizard);
            numberOfWizards++;
        } else {
            System.out.printf("%s is not allowed to enter!%n", wizard);
        }
    }
}
