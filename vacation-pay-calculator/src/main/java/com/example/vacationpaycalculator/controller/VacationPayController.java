package com.example.vacationpaycalculator.controller;

import com.example.vacationpaycalculator.service.VacationPayService;
import lombok.AllArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.DayOfWeek;
import java.time.LocalDate;

@RestController
@AllArgsConstructor
public class VacationPayController {

    @Autowired
    private final VacationPayService vacationPayService;

//    @GetMapping("/calculate")
//    public Integer getVacationPay(
//            @RequestParam Integer salary,
//            @RequestParam Integer vacationDays
//    ) {
//        return (int) ((double) salary / 29.3 * vacationDays);
//    }

    @GetMapping("/calculate")
    public Integer calculateVacationPay(
            @RequestParam Integer salary,
            @RequestParam(name = "start") @DateTimeFormat(pattern = "dd-MM-yyyy") LocalDate vacationStartDate,
            @RequestParam(name = "end") @DateTimeFormat(pattern = "dd-MM-yyyy") LocalDate vacationEndDate
            ) {
        return vacationPayService.calculateVacationPay(salary, vacationStartDate, vacationEndDate);
    }
}
