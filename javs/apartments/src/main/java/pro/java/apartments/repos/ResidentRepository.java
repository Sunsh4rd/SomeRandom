package pro.java.apartments.repos;

import pro.java.apartments.domain.resident.Resident;

import java.util.Optional;

public interface ResidentRepository {
    Optional<Resident> findById(Long id);

    void update(Resident resident);

    void create(Resident resident);

    void delete(Long id);
}
