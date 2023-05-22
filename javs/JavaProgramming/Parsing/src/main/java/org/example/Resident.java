package org.example;

import com.fasterxml.jackson.annotation.JsonValue;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Objects;

@Data
@Builder
@AllArgsConstructor
@NoArgsConstructor
public class Resident {
    private String firstName;
    private String lastName;
    private String birthDate;

    public Resident(String residentData) {
        var data = residentData.split(" ");
        this.firstName = data[0];
        this.lastName = data[1];
        this.birthDate = data[2];
    }

    @Override
    @JsonValue
    public String toString() {
        return firstName + " " + lastName + " " + birthDate;
    }
}
