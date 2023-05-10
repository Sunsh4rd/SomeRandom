package pro.java.apartments.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import pro.java.apartments.model.Apartment;

import java.util.Optional;

@Repository
public interface ApartmentRepository extends JpaRepository<Apartment, Long> {

    @Query("SELECT a FROM Apartment a WHERE a.streetName = ?1 AND a.buildingNumber = ?2 AND a.apartmentNumber = ?3")
    Optional<Apartment> findApartmentByAddress(String streetName, int buildingNumber, int apartmentNumber);
}
