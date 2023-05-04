package pro.java.apartments.repos.impl;

import org.springframework.stereotype.Repository;
import pro.java.apartments.domain.apartment.Apartment;
import pro.java.apartments.repos.ApartmentRepository;

import java.util.Optional;

@Repository
public class ApartmentRepositoryImpl implements ApartmentRepository {
    @Override
    public Optional<Apartment> findById(Long id) {
        return Optional.empty();
    }

    @Override
    public void update(Apartment apartment) {

    }

    @Override
    public void create(Apartment apartment) {

    }

    @Override
    public void delete(Long id) {

    }
}
