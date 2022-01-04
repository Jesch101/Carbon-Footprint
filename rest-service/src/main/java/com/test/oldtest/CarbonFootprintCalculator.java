package com.test.oldtest;

public class CarbonFootprintCalculator {

    private final String car_make;
    private final String car_model;
    private final String car_year;

    public CarbonFootprintCalculator(String car_make, String car_model, String car_year) {
        this.car_make = car_make;
        this.car_model = car_model;
        this.car_year = car_year;
    }

    public String getCarMake() {
        return car_make;
    }

    public String getCarModel() {
        return car_model;
    }

    public String getYear() {
        return car_year;
    }
}
