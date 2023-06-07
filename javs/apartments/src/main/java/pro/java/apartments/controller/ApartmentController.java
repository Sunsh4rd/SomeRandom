package pro.java.apartments.controller;

import lombok.AllArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pro.java.apartments.entity.Apartment;
import pro.java.apartments.repository.ApartmentRepository;

import java.util.List;

@RestController
@RequestMapping("apartments")
@AllArgsConstructor
public class ApartmentController {

    private final ApartmentRepository apartmentRepository;

    @GetMapping
    public List<Apartment> getAllApartments() {
        return apartmentRepository.findAll();
    }
}
