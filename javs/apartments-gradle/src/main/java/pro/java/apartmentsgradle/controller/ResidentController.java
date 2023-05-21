package pro.java.apartmentsgradle.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import pro.java.apartmentsgradle.entity.Resident;
import pro.java.apartmentsgradle.repository.ResidentRepository;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/residents")
public class ResidentController {

    private final ResidentRepository residentRepository;

    @GetMapping
    public List<Resident> getAllResidents() {
        return residentRepository.findAll();
    }

    @PostMapping
    public Resident addResident(
            @RequestBody Resident resident
    ) {
        return residentRepository.save(resident);
    }
}
