package pro.java.apartments.service;

import jakarta.transaction.Transactional;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pro.java.apartments.dto.ApartmentDTO;
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

    public Apartment addNewApartment(ApartmentDTO dto) {
        Apartment apartment = Apartment.builder()
                .streetName(dto.getStreetName())
                .buildingNumber(dto.getBuildingNumber())
                .apartmentNumber(dto.getApartmentNumber())
                .overallSpace(dto.getOverallSpace())
                .livingSpace(dto.getLivingSpace())
                .numberOfRooms(dto.getNumberOfRooms())
                .floor(dto.getFloor())
                .hasElevator(dto.isHasElevator())
                .hasConcierge(dto.isHasConcierge())
                .hasPrivateArea(dto.isHasPrivateArea())
                .hasParkingLot(dto.isHasParkingLot())
                .build();
//        Optional<Apartment> apartmentByAddress = apartmentRepository
//                .findApartmentByAddress(
//                        apartment.getStreetName(),
//                        apartment.getBuildingNumber(),
//                        apartment.getApartmentNumber()
//                );
//        if (apartmentByAddress.isPresent()) {
//            throw new IllegalStateException("address taken");
//        }
        return apartmentRepository.save(apartment);
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
