package org.example;

import com.fasterxml.jackson.annotation.JsonValue;

import java.time.LocalDate;
import java.util.Objects;

public class Resident {
    private String firstName;
    private String lastName;
    private String birthDate;

    public Resident() {}

    public Resident(String residentData) {
        var data = residentData.split(" ");
        this.firstName = data[0];
        this.lastName = data[1];
        this.birthDate = data[2];
    }

    public Resident(String firstName, String lastName, String birthDate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthDate = birthDate;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public String getBirthDate() {
        return birthDate;
    }

    public void setBirthDate(String birthDate) {
        this.birthDate = birthDate;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Resident resident = (Resident) o;
        return Objects.equals(firstName, resident.firstName)
                && Objects.equals(lastName, resident.lastName)
                && Objects.equals(birthDate, resident.birthDate);
    }

    @Override
    public int hashCode() {
        return Objects.hash(firstName, lastName, birthDate);
    }

    @Override
    @JsonValue
    public String toString() {
        return firstName + " " + lastName + " " + birthDate;
    }
}
