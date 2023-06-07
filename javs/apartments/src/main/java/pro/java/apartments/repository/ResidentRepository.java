package pro.java.apartments.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import pro.java.apartments.entity.Resident;

public interface ResidentRepository extends JpaRepository<Resident, Long> {
}
