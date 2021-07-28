package main;

import io.InputAndOutput;
import person.Person;

import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        Person jackson = InputAndOutput.deserialize("src/main/resources/person.json");

        System.out.println("JSON read");
        System.out.println(jackson);

        InputAndOutput.serialize(jackson);

        System.out.println("JSON wrote");
    }
}
