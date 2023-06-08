package pro.java.apartments.controller;

import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import pro.java.apartments.entity.Apartment;
import pro.java.apartments.factory.ApartmentDtoFactory;
import pro.java.apartments.repository.ApartmentRepository;

import java.util.List;

@RestController
@RequestMapping("apartments")
@RequiredArgsConstructor
@Transactional
public class ApartmentController {

    private final ApartmentRepository apartmentRepository;
    private final ApartmentDtoFactory apartmentDtoFactory;

    @GetMapping
    public List<Apartment> getAllApartments() {
        return apartmentRepository.findAll();
    }
}
