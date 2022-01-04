package com.test.oldtest;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class AdditionController {

    private static final String template = "Hello, %s!";

    //Example: /addition?firstNum=5&secondNum=3
    @GetMapping("/addition")
    public Addition addition(@RequestParam(value = "firstNum", defaultValue = "0") double firstNum,
                             @RequestParam(value = "secondNum", defaultValue = "0") double secondNum) {
        return new Addition(firstNum, secondNum, firstNum+secondNum);
    }
}