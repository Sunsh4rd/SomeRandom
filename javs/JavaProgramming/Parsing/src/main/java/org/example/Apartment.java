package org.example;

import com.fasterxml.jackson.annotation.JsonCreator;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;

import java.time.LocalDate;
import java.util.List;
import java.util.Map;
import java.util.Objects;

public class Apartment {
    private final String address;
    private final int overallSpace;
    private int livingSpace;
    public final int floor;
    private boolean hasElevator;
    private boolean hasConcierge;
    private boolean hasPrivateArea;
    private boolean hasParkingLot;
    private List<Resident> previousOwners;

    @JsonDeserialize(keyUsing = ResidentDeserializer.class)
    private Map<Resident, String> residents;

    public Apartment() {
        this.address = "";
        this.overallSpace = 0;
        this.floor = 0;
    }

    public Apartment(String address,
                     int overallSpace,
                     int livingSpace,
                     int floor,
                     boolean hasElevator,
                     boolean hasConcierge,
                     boolean hasPrivateArea,
                     boolean hasParkingLot,
                     List<Resident> previousOwners,
                     Map<Resident, String> residents) {
        this.address = address;
        this.overallSpace = overallSpace;
        this.livingSpace = livingSpace;
        this.floor = floor;
        this.hasElevator = hasElevator;
        this.hasConcierge = hasConcierge;
        this.hasPrivateArea = hasPrivateArea;
        this.hasParkingLot = hasParkingLot;
        this.previousOwners = previousOwners;
        this.residents = residents;
    }

    public String getAddress() {
        return address;
    }

    public float getOverallSpace() {
        return overallSpace;
    }

    public float getLivingSpace() {
        return livingSpace;
    }

    public void setLivingSpace(int livingSpace) {
        this.livingSpace = livingSpace;
    }

    public int getFloor() {
        return floor;
    }

    public boolean isHasElevator() {
        return hasElevator;
    }

    public void setHasElevator(boolean hasElevator) {
        this.hasElevator = hasElevator;
    }

    public boolean isHasConcierge() {
        return hasConcierge;
    }

    public void setHasConcierge(boolean hasConcierge) {
        this.hasConcierge = hasConcierge;
    }

    public boolean isHasPrivateArea() {
        return hasPrivateArea;
    }

    public void setHasPrivateArea(boolean hasPrivateArea) {
        this.hasPrivateArea = hasPrivateArea;
    }

    public boolean isHasParkingLot() {
        return hasParkingLot;
    }

    public void setHasParkingLot(boolean hasParkingLot) {
        this.hasParkingLot = hasParkingLot;
    }

    public List<Resident> getPreviousOwners() {
        return previousOwners;
    }

    public void setPreviousOwners(List<Resident> previousOwners) {
        this.previousOwners = previousOwners;
    }

    public Map<Resident, String> getResidents() {
        return residents;
    }

    public void setResidents(Map<Resident, String> residents) {
        this.residents = residents;
    }

    @Override
    public String toString() {
        return "Apartment{" +
                "address='" + address + '\'' +
                ", overallSpace=" + overallSpace +
                ", livingSpace=" + livingSpace +
                ", floor=" + floor +
                ", hasElevator=" + hasElevator +
                ", hasConcierge=" + hasConcierge +
                ", hasPrivateArea=" + hasPrivateArea +
                ", hasParkingLot=" + hasParkingLot +
                ", previousOwners=" + previousOwners +
                ", residents=" + residents +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Apartment apartment = (Apartment) o;
        return Float.compare(apartment.overallSpace, overallSpace) == 0
                && Float.compare(apartment.livingSpace, livingSpace) == 0
                && floor == apartment.floor
                && hasElevator == apartment.hasElevator
                && hasConcierge == apartment.hasConcierge
                && hasPrivateArea == apartment.hasPrivateArea
                && hasParkingLot == apartment.hasParkingLot
                && Objects.equals(address, apartment.address)
                && Objects.equals(previousOwners, apartment.previousOwners)
                && Objects.equals(residents, apartment.residents);
    }

    @Override
    public int hashCode() {
        return Objects.hash(address,
                overallSpace,
                livingSpace,
                floor,
                hasElevator,
                hasConcierge,
                hasPrivateArea,
                hasParkingLot,
                previousOwners,
                residents);
    }
}
