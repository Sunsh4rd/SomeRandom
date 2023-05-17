package pro.java.apartments.dto;

import lombok.Data;

import java.time.LocalDate;

@Data
public class ResidentDTO {
    private String firstName;
    private String lastName;
    private LocalDate birthDate;
    private long apartmentId;
}
