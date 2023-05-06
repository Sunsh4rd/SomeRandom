package pro.java.apartments.apartment;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.util.List;

@Configuration
public class ApartmentConfig {

    @Bean
    CommandLineRunner commandLineRunner(ApartmentRepository apartmentRepository) {
        return args -> {
            Apartment firstApartment = new Apartment(
                    "1-я улица",
                    5,
                    7,
                    80,
                    80,
                    4,
                    5,
                    true,
                    true,
                    true,
                    true
            );
            Apartment secondApartment = new Apartment(
                    "2-я улица",
                    4,
                    3,
                    60,
                    60,
                    3,
                    4,
                    true,
                    true,
                    true,
                    true
            );
            apartmentRepository.saveAll(
                    List.of(firstApartment, secondApartment)
            );
        };
    }
}
