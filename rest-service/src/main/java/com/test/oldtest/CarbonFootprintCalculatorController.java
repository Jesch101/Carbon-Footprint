package com.test.oldtest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;



@RestController
public class CarbonFootprintCalculatorController {

    // Example:/carbonfootprint?car_make=Nissan&car_model=Three&car_year=2020
    @GetMapping("carbonfootprint")
    public CarbonFootprintCalculator carbonFootprintCalculator(
            @RequestParam(value = "car_make", defaultValue = "") String car_make,
             @RequestParam(value = "car_model", defaultValue = "") String car_model,
             @RequestParam(value = "car_year", defaultValue = "") String car_year) {

        if (car_make.equals("BMW")) {

        } else if (car_make.equals("Toyota")) {

        } else if (car_make.equals("Nissan")) {

        } else if (car_make.equals("Ford")) {

        } else if (car_make.equals("Mustang")) {

        } else {

        }

        return new CarbonFootprintCalculator(car_make, car_model, car_year);
    }

//    @GetMapping("/addition")
//    public Addition addition(@RequestParam(value = "firstNum", defaultValue = "0") double firstNum,
//                             @RequestParam(value = "secondNum", defaultValue = "0") double secondNum) {
//        return new Addition(firstNum, secondNum, firstNum+secondNum);
//    }

}
