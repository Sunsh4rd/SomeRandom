package pro.java.apartments.controller;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;
import pro.java.apartments.dto.ResidentDto;
import pro.java.apartments.entity.Resident;
import pro.java.apartments.factory.ResidentDtoFactory;
import pro.java.apartments.repository.ResidentRepository;

import java.time.LocalDate;
import java.util.List;

@RestController
@RequestMapping("residents")
@RequiredArgsConstructor
@Transactional
public class ResidentController {

    private final ResidentRepository residentRepository;
    private final ResidentDtoFactory residentDtoFactory;

    @GetMapping
    public List<Resident> getAllResidents() {
        return residentRepository.findAll();
    }

    @PostMapping
    public ResidentDto addNewResident(
            @RequestParam String firstName,
            @RequestParam String lastName,
            @RequestParam LocalDate birthDate,
            @RequestParam String gender
    ) {
        Resident newResident = residentRepository.saveAndFlush(
                Resident.builder()
                        .firstName(firstName)
                        .lastName(lastName)
                        .birtDate(birthDate)
                        .gender(gender)
                        .build()
        );
        return residentDtoFactory.makeResidentDto(newResident);
    }
}
