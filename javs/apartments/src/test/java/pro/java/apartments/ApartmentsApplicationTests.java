package pro.java.apartments;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import pro.java.apartments.entity.Apartment;
import pro.java.apartments.entity.Resident;
import pro.java.apartments.repository.ApartmentRepository;
import pro.java.apartments.repository.ResidentRepository;

import java.time.LocalDate;
import java.time.Month;

@SpringBootTest
class ApartmentsApplicationTests {

	@Autowired
	ApartmentRepository apartmentRepository;

	@Autowired
	ResidentRepository residentRepository;

//	@Test
//	void contextLoads() {
//	}

	@Test
	void testInsert() {
		var apartment = Apartment.builder()
				.streetName("1-я улица")
				.buildingNumber(1)
				.apartmentNumber(25)
				.overallSpace(80)
				.livingSpace(80)
				.numberOfRooms(4)
				.floor(6)
				.hasElevator(true)
				.hasConcierge(true)
				.hasPrivateArea(true)
				.hasParkingLot(true)
				.build();
		assertEquals(apartment, apartmentRepository.save(apartment));
		assertNotNull(apartmentRepository.findAll());
		var resident = Resident.builder()
				.firstName("Иван")
				.lastName("Иванов")
				.birtDate(LocalDate.of(1990, Month.JANUARY, 1))
				.gender("M")
				.apartment(apartment)
				.build();
		assertEquals(resident, residentRepository.save(resident));
		assertNotNull(residentRepository.findAll());
	}
}

//"buildingNumber": 1,
//		"apartmentNumber": 25,
//		"overallSpace": 80,
//		"livingSpace": 80,
//		"numberOfRooms": 4,
//		"floor": 6,
//		"hasElevator": true,
//		"hasConcierge": true,
//		"hasPrivateArea": true,
//		"hasParkingLot": true,
//		"previousOwners": [
//		"Вася Пупкин 01.01.1990",
//		"Петр Петров 02.03.1990"
//		],
//		"residents": {
//		"Иван Иванов 02.02.1991": "31.12.2030"
//		}
//		},
