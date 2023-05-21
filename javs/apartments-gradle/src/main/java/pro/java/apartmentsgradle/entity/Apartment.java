package pro.java.apartmentsgradle.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.List;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Builder
public class Apartment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
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

    @OneToMany
    @JoinColumn(name = "resident_id")
    private List<Resident> residents;
}
