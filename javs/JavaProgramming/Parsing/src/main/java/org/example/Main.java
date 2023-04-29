package org.example;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        var apartmentList = List.of(
                new Apartment("1-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("2-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("2-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("3-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("4-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("5-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("6-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("7-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("8-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("9-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("10-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("11-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("12-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                ),
                new Apartment("2-я улица", 80, 80, 7, true, true, true, true,
                        List.of(new Resident("Vasya", "Pupkin", "01.01.1990")),
                        Map.of(new Resident("Masha", "Ivanova", "01.01.1991"), "31.12.2030")
                )
        );

        var objectMapper = new ObjectMapper();
        try {
            objectMapper.writeValue(new File("apartments.json"), apartmentList);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
        try {
            var apartmentStream = Stream.of(
                    objectMapper.readValue(new File("apartments.json"), new TypeReference<List<Apartment>>() {
                    })
            );
            apartmentStream.forEach(System.out::println);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}