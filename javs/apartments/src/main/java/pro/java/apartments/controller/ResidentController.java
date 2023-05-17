package pro.java.apartments.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pro.java.apartments.dto.ResidentDTO;
import pro.java.apartments.model.Resident;
import pro.java.apartments.service.ResidentService;

import java.util.List;

@RestController
@RequestMapping(path = "/residents")
public class ResidentController {

    @Autowired
    private final ResidentService residentService;

    public ResidentController(ResidentService residentService) {
        this.residentService = residentService;
    }

    @GetMapping
    public List<Resident> getResidents() {
        return residentService.getResidents();
    }

    @PostMapping
    public ResponseEntity<Resident> registerNewResident(@RequestBody ResidentDTO dto) {
        return new ResponseEntity<>(residentService.addNewResident(dto), HttpStatus.OK);
    }
}
