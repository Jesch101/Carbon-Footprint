package com.test.oldtest;

public class EmissionsCalculator {

    private final double milesPerGallon;
    private final double milesTraveled;
    private final double fuelEfficiency;

    public EmissionsCalculator(double milesPerGallon, double milesTraveled, double fuelEfficiency) {
        this.milesPerGallon = milesPerGallon;
        this.milesTraveled = milesTraveled;
        this.fuelEfficiency = fuelEfficiency;
    }

    public double getMilesPerGallon() {
        return milesPerGallon;
    }

    public double getMilesTraveled() {
        return milesTraveled;
    }

    public double getFuelEfficiency() {
        return fuelEfficiency;
    }
}
