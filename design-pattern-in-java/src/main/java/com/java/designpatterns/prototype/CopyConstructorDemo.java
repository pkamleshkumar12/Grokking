package com.java.designpatterns.prototype;

class Address1 {

    public String streetAddress, city, country;

    public Address1(String streetAddress, String city, String country) {
        this.streetAddress = streetAddress;
        this.city = city;
        this.country = country;
    }

    public Address1(Address1 other){
        this(other.streetAddress, other.city, other.country);
    }

    @Override
    public String toString() {
        return "Address1{" +
                "streetAddress='" + streetAddress + '\'' +
                ", city='" + city + '\'' +
                ", country='" + country + '\'' +
                '}';
    }
}

class Employee {

    public String name;
    public Address1 address1;

    public Employee(String name, Address1 address1) {
        this.name = name;
        this.address1 = address1;
    }

    @Override
    public String toString() {
        return "Employee{" +
                "name='" + name + '\'' +
                ", address1=" + address1 +
                '}';
    }

    public Employee(Employee other){
        name = other.name;
        address1 = new Address1(other.address1);
    }
}
public class CopyConstructorDemo {

    public static void main(String[] args) {

        Employee will = new Employee("will",new Address1("Bakers street", "london", "uk"));
        Employee jane = new Employee(will);
        jane.name = "jane";
        jane.address1.streetAddress = "China town";

        System.out.println(will);
        System.out.println(jane);
    }
}
