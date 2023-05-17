package pro.java.apartments.controller;

import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pro.java.apartments.dto.ApartmentDTO;
import pro.java.apartments.model.Apartment;
import pro.java.apartments.service.ApartmentService;

import java.util.List;

@RestController
@RequestMapping(path = "/apartments")
@Tag(name = "Apartments", description = "apts methods")
public class ApartmentController {

    private final ApartmentService apartmentService;

    @Autowired
    public ApartmentController(ApartmentService apartmentService) {
        this.apartmentService = apartmentService;
    }

    @GetMapping
    public List<Apartment> getApartments() {
        return apartmentService.getApartments();
    }

    @PostMapping
    public ResponseEntity<Apartment> registerNewApartment(@RequestBody ApartmentDTO dto) {
        return new ResponseEntity<>(apartmentService.addNewApartment(dto), HttpStatus.OK);
    }

    @DeleteMapping("{apartmentId}")
    public void deleteApartment(@PathVariable("apartmentId") Long apartmentId) {
        apartmentService.deleteApartment(apartmentId);
    }

    @PutMapping("{apartmentId}")
    public void updateApartment(@PathVariable("apartmentId") Long apartmentId,
                                @RequestParam(required = false) Integer livingSpace,
                                @RequestParam(required = false) Integer numberOfRooms) {
        apartmentService.updateApartment(apartmentId, livingSpace, numberOfRooms);
    }
}
