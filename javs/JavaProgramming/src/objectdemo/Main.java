package objectdemo;

public class Main {

    public static void main(String[] args) {
        var someEntity = new SomeEntity(1, "name");
        System.out.println(someEntity); //toString

        try {
            var someEntityClone = someEntity.clone();
            System.out.println("== " + (someEntity == someEntityClone));
            System.out.println("equals " + someEntity.equals(someEntityClone));
        } catch (CloneNotSupportedException e) {
            throw new RuntimeException(e);
        }

        System.out.println(someEntity.getClass());

        Data data = new Data();
        Thread sender = new Thread(new Sender(data));
        Thread receiver = new Thread(new Receiver(data));

        sender.start();
        receiver.start();
    }
}
