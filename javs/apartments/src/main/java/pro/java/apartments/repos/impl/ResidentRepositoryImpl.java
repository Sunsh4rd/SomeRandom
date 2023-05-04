package pro.java.apartments.repos.impl;

import org.springframework.stereotype.Repository;
import pro.java.apartments.domain.resident.Resident;
import pro.java.apartments.repos.ResidentRepository;

import java.util.Optional;

@Repository
public class ResidentRepositoryImpl implements ResidentRepository {
    @Override
    public Optional<Resident> findById(Long id) {
        return Optional.empty();
    }

    @Override
    public void update(Resident resident) {

    }

    @Override
    public void create(Resident resident) {

    }

    @Override
    public void delete(Long id) {

    }
}
