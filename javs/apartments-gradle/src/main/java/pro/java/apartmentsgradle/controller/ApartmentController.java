package pro.java.apartmentsgradle.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.*;
import pro.java.apartmentsgradle.entity.Apartment;
import pro.java.apartmentsgradle.repository.ApartmentRepository;

import java.util.List;

@RestController
@AllArgsConstructor
@RequestMapping("/apartments")
public class ApartmentController {

    private final ApartmentRepository apartmentRepository;

    @GetMapping
    public List<Apartment> getAllApartments() {
        return apartmentRepository.findAll();
    }

    @PostMapping
    public Apartment addApartment(
            @RequestBody Apartment apartment
    ) {
        return apartmentRepository.save(apartment);
    }
}
