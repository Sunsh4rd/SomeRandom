package patterns.proxy;

public class Main {
    public static void main(String[] args) {
        var proxy = new WizardTowerProxy(new IvoryTower());
        proxy.enter(new Wizard("Red Wizard"));
        proxy.enter(new Wizard("Green Wizard"));
        proxy.enter(new Wizard("Blue Wizard"));
        proxy.enter(new Wizard("White Wizard"));
        proxy.enter(new Wizard("Black Wizard"));
    }
}
