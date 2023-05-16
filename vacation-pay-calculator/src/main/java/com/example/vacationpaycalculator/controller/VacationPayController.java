package com.example.vacationpaycalculator.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class VacationPayController {

    @GetMapping("/calculate")
    public String getVacationPay(
            @RequestParam Integer salary,
            @RequestParam Integer vacationDays
    ) {
//        return salary / (int) 29.3 * vacationDays;
        return "calculation";
    }
}
