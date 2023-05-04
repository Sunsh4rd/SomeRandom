package pro.java.apartments.domain.resident;

import lombok.Data;

@Data
public class Resident {
    private Long id;
    private String firstName;
    private String lastName;
    private String birthDate;
}
