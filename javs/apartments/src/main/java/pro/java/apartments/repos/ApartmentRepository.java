package pro.java.apartments.repos;

import pro.java.apartments.domain.apartment.Apartment;

import java.util.Optional;

public interface ApartmentRepository {
    Optional<Apartment> findById(Long id);

    void update(Apartment apartment);

    void create(Apartment apartment);

    void delete(Long id);
}
