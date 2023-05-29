package pro.java.apartments;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import pro.java.apartments.model.Resident;
import pro.java.apartments.repository.ApartmentRepository;
import pro.java.apartments.repository.ResidentRepository;

import java.time.LocalDate;
import java.time.Month;

@SpringBootTest
class ApartmentsApplicationTests {

    @Autowired
    private ApartmentRepository apartmentRepository;

    @Autowired
    private ResidentRepository residentRepository;

    @Test
    void contextLoads() {
    }

    @Test
    void createNewResident() {
        System.out.println(apartmentRepository.findById(1L).get());
        Resident resident = Resident.builder()
                .firstName("Иван")
                .lastName("Иванов")
                .birthDate(LocalDate.of(1995, Month.JANUARY, 1))
                .apartment(apartmentRepository.findById(1L).orElseThrow(
                        () -> new IllegalStateException("No such apartment")
                )).build();
        assertEquals(resident, residentRepository.save(resident));
    }
}
