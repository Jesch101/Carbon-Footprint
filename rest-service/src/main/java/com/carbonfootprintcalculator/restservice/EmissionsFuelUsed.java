package com.carbonfootprintcalculator.restservice;

import java.math.BigDecimal;

/*
 * Calculate the CO2 produced in kg given the gallons of fuel used.
 */
public class EmissionsFuelUsed {

    private final double fuelUsedInGallons;
    private final BigDecimal carbonDioxideProducedInKg;

    public EmissionsFuelUsed(double fuelUsedInGallons, BigDecimal carbonDioxideProducedInKg) {
        this.fuelUsedInGallons = fuelUsedInGallons;
        this.carbonDioxideProducedInKg = carbonDioxideProducedInKg;
    }

    public double getFuelUsedInGallons() {
        return fuelUsedInGallons;
    }

    public BigDecimal getCarbonDioxideProducedInKg() {
        return carbonDioxideProducedInKg;
    }
}
