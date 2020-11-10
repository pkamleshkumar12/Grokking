package com.java.designpatterns.prototype;

import java.util.Arrays;

class Address implements Cloneable {

    public String streetName;
    public int houseNumber;

    public Address(String streetName, int houseNumber) {
        this.streetName = streetName;
        this.houseNumber = houseNumber;
    }

    @Override
    public String toString() {
        return "Address{" +
                "streetName='" + streetName + '\'' +
                ", houseNumber=" + houseNumber +
                '}';
    }

    // deep copy
    @Override
    public Object clone() throws CloneNotSupportedException {
        return new Address(streetName, houseNumber);
    }
}

class Person implements Cloneable {

    public String[] name;
    public Address address;

    public Person(String[] name, Address address) {
        this.name = name;
        this.address = address;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name=" + Arrays.toString(name) +
                ", address=" + address +
                '}';
    }

    @Override
    public Object clone() throws CloneNotSupportedException {
        return new Person(
                name.clone(),
                (Address) address.clone());
    }
}


public class CloneDemo {

    public static void main(String[] args) throws Exception {

        Person will = new Person(new String[]{"will", "smith"}, new Address("Bakers street", 123));
        Person jane = (Person) will.clone();
        jane.name[0] = "jane";
        jane.address.houseNumber = 124;

        System.out.println(will);
        System.out.println(jane);


    }
}
