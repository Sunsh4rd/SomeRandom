package pro.java.apartments.factory;

import org.springframework.stereotype.Component;
import pro.java.apartments.dto.ResidentDto;
import pro.java.apartments.entity.Resident;

@Component
public class ResidentDtoFactory {
    public ResidentDto makeResidentDto(Resident resident) {
        return ResidentDto.builder()
                .id(resident.getId())
                .firstName(resident.getFirstName())
                .lastName(resident.getLastName())
                .birtDate(resident.getBirtDate())
                .gender(resident.getGender())
                .build();
    }
}
