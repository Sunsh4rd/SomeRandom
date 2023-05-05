package pro.java.apartments.resident;

import lombok.AllArgsConstructor;
import lombok.Data;

import java.time.LocalDate;

@Data
@AllArgsConstructor
public class Resident {
    private Long id;
    private String firstName;
    private String lastName;
    private LocalDate birthDate;
}
