package pro.java.apartments.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDate;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ResidentDto {
    private Long id;
    private String firstName;
    private String lastName;
    private LocalDate birtDate;
    private String gender;
//    private Apartment apartment;
}
