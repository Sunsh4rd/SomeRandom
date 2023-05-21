package pro.java.apartmentsgradle.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import pro.java.apartmentsgradle.entity.Resident;

@Repository
public interface ResidentRepository extends JpaRepository<Resident, Long> {
}
