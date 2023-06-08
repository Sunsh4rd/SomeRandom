package pro.java.apartments.factory;

import org.springframework.stereotype.Component;
import pro.java.apartments.dto.ApartmentDto;
import pro.java.apartments.entity.Apartment;

@Component
public class ApartmentDtoFactory {
    public ApartmentDto makeApartmentDto(Apartment apartment) {
        return ApartmentDto.builder()
                .id(apartment.getId())
                .streetName(apartment.getStreetName())
                .buildingNumber(apartment.getBuildingNumber())
                .apartmentNumber(apartment.getApartmentNumber())
                .overallSpace(apartment.getOverallSpace())
                .livingSpace(apartment.getLivingSpace())
                .numberOfRooms(apartment.getNumberOfRooms())
                .floor(apartment.getFloor())
                .hasConcierge(apartment.isHasConcierge())
                .hasParkingLot(apartment.isHasParkingLot())
                .hasElevator(apartment.isHasElevator())
                .hasPrivateArea(apartment.isHasPrivateArea())
                .build();
    }
}
