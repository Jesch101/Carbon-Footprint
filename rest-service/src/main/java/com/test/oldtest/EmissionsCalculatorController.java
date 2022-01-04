package com.test.oldtest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
@RestController
public class EmissionsCalculatorController {

    @GetMapping("emissionscalculator")
    public EmissionsCalculator emissionsCalculator(
            @RequestParam(value = "milesPerGallon", defaultValue = "") double milesPerGallon,
            @RequestParam(value = "milesTraveled", defaultValue = "") double milesTraveled) {
        double calculatedFuelEfficiency = (milesPerGallon * milesTraveled) / 100;
        return new EmissionsCalculator(milesPerGallon, milesTraveled, calculatedFuelEfficiency);
    }

}
