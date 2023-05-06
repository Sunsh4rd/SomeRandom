package pro.java.apartments.apartment;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;


@Data
@Entity
@Table
@NoArgsConstructor
public class Apartment {
    @Id
    @SequenceGenerator(
            name = "apartment_sequence",
            sequenceName = "apartment_sequence",
            allocationSize = 1
    )
    @GeneratedValue(
            strategy = GenerationType.SEQUENCE,
            generator = "apartment_sequence"
    )
    private Long id;
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

    public Apartment(String streetName,
                     int buildingNumber,
                     int apartmentNumber,
                     int overallSpace,
                     int livingSpace,
                     int numberOfRooms,
                     int floor,
                     boolean hasElevator,
                     boolean hasConcierge,
                     boolean hasPrivateArea,
                     boolean hasParkingLot) {
        this.streetName = streetName;
        this.buildingNumber = buildingNumber;
        this.apartmentNumber = apartmentNumber;
        this.overallSpace = overallSpace;
        this.livingSpace = livingSpace;
        this.numberOfRooms = numberOfRooms;
        this.floor = floor;
        this.hasElevator = hasElevator;
        this.hasConcierge = hasConcierge;
        this.hasPrivateArea = hasPrivateArea;
        this.hasParkingLot = hasParkingLot;
    }
    //    private List<Resident> previousOwners;
//    private Map<Resident, LocalDate> registeredResidents;
}
