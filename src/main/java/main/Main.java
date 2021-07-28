package main;

import com.fasterxml.jackson.databind.ObjectMapper;
import person.Person;

import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        Person person = deserialize("src/main/resources/generated.json");

        System.out.println("Json read");
        System.out.println(person);

        serialize(person);

        System.out.println("Json wrote");
    }

    private static Person deserialize(String fileName) throws IOException {

        ObjectMapper objectMapper = new ObjectMapper();

        try (InputStream inputStream = new FileInputStream(fileName)) {

            return objectMapper.readValue(inputStream, Person.class);
        }
    }

    private static void serialize(Object object) throws IOException {

        ObjectMapper objectMapper = new ObjectMapper();

        try (OutputStream outputStream = new FileOutputStream("output/out.json")) {

            objectMapper.writeValue(outputStream, object);
        }
    }
}
