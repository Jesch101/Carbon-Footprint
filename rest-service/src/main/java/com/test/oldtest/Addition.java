package com.test.oldtest;

public class Addition {

    private final double firstNum;

    private final double secondNum;

    private final double sum;

    public Addition(double firstNum, double secondNum, double sum) {
        this.firstNum = firstNum;
        this.secondNum = secondNum;
        this.sum = sum;
    }

    public double getFirstNum() {
        return firstNum;
    }

    public double getSecondNum() {
        return secondNum;
    }

    public double getSum() {
        return sum;
    }
}
