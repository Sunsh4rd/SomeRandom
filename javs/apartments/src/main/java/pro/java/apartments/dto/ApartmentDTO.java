package pro.java.apartments.dto;

import lombok.Data;

@Data
public class ApartmentDTO {
    private String streetName;
    private int buildingNumber;
    private int apartmentNumber;
    private int overallSpace;
    private int livingSpace;
    private int numberOfRooms;
    private int floor;
    private boolean hasElevator;
    private boolean hasConcierge;
    private boolean hasPrivateArea;
    private boolean hasParkingLot;
}
