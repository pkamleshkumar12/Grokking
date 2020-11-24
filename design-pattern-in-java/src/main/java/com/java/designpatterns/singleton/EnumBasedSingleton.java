package com.java.designpatterns.singleton;

import java.io.*;

// limitation: its not helpful in the case of serialization and deserialization
enum EnumSingleton {

    INSTANCE;

    EnumSingleton() {
        value = 42;
    }

    private int value;

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}

public class EnumBasedSingleton {

    static void saveToFile(EnumSingleton singleton, String fileName) throws Exception {

        try (FileOutputStream fileOut = new FileOutputStream(fileName);
             ObjectOutputStream out = new ObjectOutputStream(fileOut)) {
            out.writeObject(singleton);
        }
    }

    static EnumSingleton readFromFile(String filename) throws Exception {

        try (FileInputStream fileIn = new FileInputStream(filename);
             ObjectInputStream in = new ObjectInputStream(fileIn)) {
            return (EnumSingleton) in.readObject();
        }
    }

    public static void main(String[] args) throws Exception {
        String filename = "myfile.bin";

        EnumSingleton singleton = EnumSingleton.INSTANCE;
        singleton.setValue(111);
        saveToFile(singleton, filename);

        EnumSingleton singleton1 = readFromFile(filename);
        System.out.println(singleton1.getValue());
    }
}
