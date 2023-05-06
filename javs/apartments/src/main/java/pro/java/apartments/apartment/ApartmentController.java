package pro.java.apartments.apartment;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "apartments")
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
    public void registerNewApartment(@RequestBody Apartment apartment) {
        apartmentService.addNewApartment(apartment);
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
