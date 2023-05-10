package pro.java.apartments.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import pro.java.apartments.model.Resident;

import java.time.LocalDate;
import java.util.Optional;

@Repository
public interface ResidentRepository extends JpaRepository<Resident, Long> {

    @Query("SELECT r FROM Resident r WHERE r.firstName = ?1 AND r.lastName = ?2 AND r.birthDate = ?3")
    Optional<Resident> findSpecificResident(String firstName, String lastName, LocalDate birthDate);
}
