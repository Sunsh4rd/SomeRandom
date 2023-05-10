package pro.java.apartments.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
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
    public void registerNewResident(@RequestBody Resident resident) {
        residentService.addNewResident(resident);
    }
}
