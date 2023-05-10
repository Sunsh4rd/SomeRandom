package pro.java.apartments.model;

import jakarta.persistence.*;
import lombok.*;

import java.util.List;



@Entity
@Table
@Data
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

    @OneToMany(mappedBy = "apartment")
    private List<Resident> residents;

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
                     boolean hasParkingLot,
                     List<Resident> residents) {
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
        this.residents = residents;
    }
}
