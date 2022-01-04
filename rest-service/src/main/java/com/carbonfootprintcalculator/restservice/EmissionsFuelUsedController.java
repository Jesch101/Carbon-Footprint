package com.carbonfootprintcalculator.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.math.BigDecimal;

/* Handles the logic for the calculation of the Carbon emission given the fuel used. */
@RestController
public class EmissionsFuelUsedController {

    @GetMapping("calculateEmissionsGivenFuelConsumed")
    public EmissionsFuelUsed emissionsCalculator(
            @RequestParam(value = "fuelUsedInGallons", defaultValue = "") double fuelUsedInGallons) {
        BigDecimal carbonDioxideProducedInKG = new BigDecimal(fuelUsedInGallons);
        carbonDioxideProducedInKG = carbonDioxideProducedInKG.multiply(new BigDecimal(String.valueOf(BigDecimal.valueOf(Constants.fuelConsumptionMultiplier))));
        return new EmissionsFuelUsed(fuelUsedInGallons, carbonDioxideProducedInKG);
    }

}
