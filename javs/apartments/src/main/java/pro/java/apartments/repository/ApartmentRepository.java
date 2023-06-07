package pro.java.apartments.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import pro.java.apartments.entity.Apartment;

public interface ApartmentRepository extends JpaRepository<Apartment, Long> {
}
