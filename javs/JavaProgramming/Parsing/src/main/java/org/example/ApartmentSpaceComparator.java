package org.example;

import java.util.Comparator;

public class ApartmentSpaceComparator implements Comparator<Apartment> {
    @Override
    public int compare(Apartment o1, Apartment o2) {
        if (o1.getOverallSpace() > o2.getOverallSpace()) {
            return 1;
        } else if (o1.getOverallSpace() < o2.getOverallSpace()) {
            return -1;
        }
        return 0;
    }
}
