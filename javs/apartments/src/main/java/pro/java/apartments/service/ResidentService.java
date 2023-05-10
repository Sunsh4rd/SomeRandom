package pro.java.apartments.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import pro.java.apartments.model.Resident;
import pro.java.apartments.repository.ResidentRepository;

import java.util.List;
import java.util.Optional;

@Service
public class ResidentService {

    private final ResidentRepository residentRepository;

    @Autowired
    public ResidentService(ResidentRepository residentRepository) {
        this.residentRepository = residentRepository;
    }

    public List<Resident> getResidents() {
        return residentRepository.findAll();
    }

    public void addNewResident(Resident resident) {
        Optional<Resident> specificResident = residentRepository
                .findSpecificResident(
                        resident.getFirstName(),
                        resident.getLastName(),
                        resident.getBirthDate()
                );
        if (specificResident.isPresent()) {
            throw new IllegalStateException("resident already exists");
        }
        residentRepository.save(resident);
    }
}
