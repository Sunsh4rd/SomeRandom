package com.example.vacationpaycalculator.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;

@Controller
public class VacationPayController {

    @GetMapping("/calculate")
    public String getVacationPay(
//            @RequestParam Integer salary,
//            @RequestParam Integer vacationDays
    ) {
//        return salary / (int) 29.3 * vacationDays;
        return "calculate";
    }

    @PostMapping("/calculate")
    @ModelAttribute("calculate")
    public String vacate() {
        return "ye";
    }
}
