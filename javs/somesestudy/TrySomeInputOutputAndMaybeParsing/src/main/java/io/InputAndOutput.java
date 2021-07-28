package io;

import com.fasterxml.jackson.databind.ObjectMapper;
import person.Person;

import java.io.*;

public class InputAndOutput {
    private static final ObjectMapper objectMapper = new ObjectMapper();

    public static void serialize(Object object) throws IOException {
        try (OutputStream outputStream = new FileOutputStream("output/out.json")) {
            objectMapper.writeValue(outputStream, object);
        }
    }

    public static Person deserialize(String fileName) throws IOException {
        try (InputStream inputStream = new FileInputStream(fileName)){
            return objectMapper.readValue(inputStream, Person.class);
        }
    }
}
