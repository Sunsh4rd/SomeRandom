package pro.java.apartments.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
@Builder
public class Apartment {

    @Id
    @GeneratedValue
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

    @Builder.Default
    @OneToMany(mappedBy = "apartment")
    private List<Resident> residents = new ArrayList<>();
}
