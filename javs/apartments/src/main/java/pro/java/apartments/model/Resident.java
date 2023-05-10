package pro.java.apartments.model;

import jakarta.persistence.*;
import lombok.*;
import pro.java.apartments.model.Apartment;

import java.time.LocalDate;

@Data
@NoArgsConstructor
@Entity
@Table
public class Resident {
    @Id
    @GeneratedValue
    private Long id;

    private String firstName;
    private String lastName;
    private LocalDate birthDate;

    @ManyToOne
    @JoinColumn(name = "apartment_id")
    private Apartment apartment;

    public Resident(String firstName, String lastName, LocalDate birthDate, Apartment apartment) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
        this.apartment = apartment;
    }
}
