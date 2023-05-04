package pro.java.apartments.domain.apartment;

import lombok.Data;
import pro.java.apartments.domain.resident.Resident;

import java.util.List;

@Data
public class Apartment {
    private Long id;
    private final String address;
    private final int overallSpace;
    private int livingSpace;
    private int numberOfRooms;
    public final int floor;
    private boolean hasElevator;
    private boolean hasConcierge;
    private boolean hasPrivateArea;
    private boolean hasParkingLot;
    private List<Resident> previousOwners;

}
