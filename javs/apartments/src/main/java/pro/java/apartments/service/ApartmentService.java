package pro.java.apartments.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pro.java.apartments.repository.ApartmentRepository;
import pro.java.apartments.model.Apartment;

import java.util.List;
import java.util.Optional;

@Service
public class ApartmentService {

    private final ApartmentRepository apartmentRepository;

    @Autowired
    public ApartmentService(ApartmentRepository apartmentRepository) {
        this.apartmentRepository = apartmentRepository;
    }

    public List<Apartment> getApartments() {
        return apartmentRepository.findAll();
    }

    public void addNewApartment(Apartment apartment) {
        Optional<Apartment> apartmentByAddress = apartmentRepository
                .findApartmentByAddress(
                        apartment.getStreetName(),
                        apartment.getBuildingNumber(),
                        apartment.getApartmentNumber()
                );
        if (apartmentByAddress.isPresent()) {
            throw new IllegalStateException("address taken");
        }
        apartmentRepository.save(apartment);
    }

    public void deleteApartment(Long apartmentId) {
        boolean exists = apartmentRepository.existsById(apartmentId);
        if (!exists) {
            throw new IllegalStateException("apartment with id " + apartmentId + " does not exist");
        }
        apartmentRepository.deleteById(apartmentId);
    }

    @Transactional
    public void updateApartment(Long apartmentId, Integer livingSpace, Integer numberOfRooms) {
        Apartment apartment = apartmentRepository.findById(apartmentId)
                .orElseThrow(() -> new IllegalStateException(
                        "apartment with id " + apartmentId + "does not exist"));

        if (livingSpace > 0 && livingSpace < apartment.getOverallSpace()) {
            apartment.setLivingSpace(livingSpace);
        }

        if (numberOfRooms > 0 && numberOfRooms != apartment.getNumberOfRooms()) {
            apartment.setNumberOfRooms(numberOfRooms);
        }
    }
}
