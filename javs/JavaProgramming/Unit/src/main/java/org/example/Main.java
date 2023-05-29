package org.example;

import java.time.LocalDate;
import java.time.Month;
import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {

        Map<LocalDate, Integer> localDateIntegerMap = new HashMap<>();

        localDateIntegerMap.put(LocalDate.of(2021, Month.MAY, 12), 1);
        System.out.println(localDateIntegerMap.get(LocalDate.of(2021,Month.SEPTEMBER,12)));

    }
}