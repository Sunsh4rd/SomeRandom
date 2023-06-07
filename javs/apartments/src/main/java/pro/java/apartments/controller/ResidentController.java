package pro.java.apartments.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import pro.java.apartments.entity.Resident;
import pro.java.apartments.repository.ResidentRepository;

import java.util.List;

@RestController
@RequestMapping("residents")
@AllArgsConstructor
public class ResidentController {

    private final ResidentRepository residentRepository;

    @GetMapping
    public List<Resident> getAllResidents() {
        return residentRepository.findAll();
    }

    @PostMapping
    public Resident addNewResident(@RequestBody Resident resident) {
        var newResident = Resident.builder()
                .firstName(resident.getFirstName())
                .lastName(resident.getLastName())
                .birtDate(resident.getBirtDate())
                .gender(resident.getGender())
                .apartment(resident.getApartment())
                .build();
        return residentRepository.save(newResident);
    }
}
