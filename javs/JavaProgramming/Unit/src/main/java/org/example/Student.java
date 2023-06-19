package org.example;

import java.math.BigDecimal;



class ClassCastExceptionExample {

    public static void main(String[] args)

    {

        // Creating a BigDecimal object

        Object sampleObject = new BigDecimal(10000000.45);

        System.out.println(String.valueOf(sampleObject));

    }

}