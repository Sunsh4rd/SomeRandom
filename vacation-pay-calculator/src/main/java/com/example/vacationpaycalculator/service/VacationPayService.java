package com.example.vacationpaycalculator.service;

import org.springframework.stereotype.Service;

import java.time.DayOfWeek;
import java.time.LocalDate;
import java.time.Month;
import java.time.temporal.ChronoUnit;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

@Service
public class VacationPayService {

    public Integer calculateVacationPay(Integer salary,
                                        LocalDate vacationStartDate,
                                        LocalDate vacationEndDate
    ) {
        long vacationDuration = Stream.iterate(vacationStartDate, d -> d.plusDays(1))
                .limit(ChronoUnit.DAYS.between(vacationStartDate, vacationEndDate) + 1)
                .filter(d -> d.getDayOfWeek() != DayOfWeek.SATURDAY && d.getDayOfWeek() != DayOfWeek.SUNDAY)
                .filter(d -> !d.equals(LocalDate.of(d.getYear(), Month.DECEMBER, 31)))
                .filter(d -> !d.equals(LocalDate.of(d.getYear(), Month.JANUARY, 1)))
                .filter(d -> !d.equals(LocalDate.of(d.getYear(), Month.FEBRUARY, 23)))
                .filter(d -> !d.equals(LocalDate.of(d.getYear(), Month.MARCH, 8)))
                .filter(d -> !d.equals(LocalDate.of(d.getYear(), Month.MAY, 9)))
                .count();
        return (int) ((double) salary / 29.3 * vacationDuration);
    }
}
