package pro.java.apartments.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pro.java.apartments.dto.ResidentDTO;
import pro.java.apartments.model.Resident;
import pro.java.apartments.repository.ApartmentRepository;
import pro.java.apartments.repository.ResidentRepository;

import java.util.List;
import java.util.Optional;

@Service
public class ResidentService {

    private final ResidentRepository residentRepository;
    private final ApartmentRepository apartmentRepository;

    @Autowired
    public ResidentService(ResidentRepository residentRepository, ApartmentRepository apartmentRepository) {
        this.residentRepository = residentRepository;
        this.apartmentRepository = apartmentRepository;
    }

    public List<Resident> getResidents() {
        return residentRepository.findAll();
    }

    public Resident addNewResident(ResidentDTO dto) {
        Resident resident = Resident.builder()
                .firstName(dto.getFirstName())
                .lastName(dto.getLastName())
                .apartment(apartmentRepository.findById(
                        dto.getApartmentId()
                ).orElseThrow(
                        () -> new IllegalStateException("No such apartment")
                )).build();
//        Optional<Resident> specificResident = residentRepository
//                .findSpecificResident(
//                        resident.getFirstName(),
//                        resident.getLastName(),
//                        resident.getBirthDate()
//                );
//        if (specificResident.isPresent()) {
//            throw new IllegalStateException("resident already exists");
//        }
        return residentRepository.save(resident);
    }
}
