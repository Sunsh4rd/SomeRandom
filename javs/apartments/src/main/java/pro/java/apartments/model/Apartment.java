package pro.java.apartments.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;


@Entity
@Table
@Data
@NoArgsConstructor
@AllArgsConstructor
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

    @OneToMany(
            cascade = CascadeType.ALL,
            fetch = FetchType.EAGER,
            mappedBy = "apartment"
    )
//    @JoinColumn(name = "resident_id")
    private List<Resident> residents;

}
