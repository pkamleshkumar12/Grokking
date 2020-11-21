package com.java.designpatterns.singleton;

import java.io.*;

class BasicSingleton implements Serializable{

    private BasicSingleton(){

    }
    private static final BasicSingleton BASIC_SINGLETON = new BasicSingleton();

    public static BasicSingleton getBasicSingleton(){
        return BASIC_SINGLETON;
    }
    private int value  = 0;

    public int getValue(){
        return value;
    }

    public void setValue(int value){
        this.value = value;
    }

    protected Object readResolve(){
        return BASIC_SINGLETON;
    }
}

public class BasicSingletonDemo {

    static void saveToFile(BasicSingleton singleton,
                           String filename) throws Exception {

        try(FileOutputStream fileOut = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(fileOut)){
            out.writeObject(singleton);
        }
    }

    static BasicSingleton readFromFile(String fileName) throws Exception {

        try (FileInputStream fileIn = new FileInputStream(fileName);
             ObjectInputStream in = new ObjectInputStream(fileIn)) {

            return (BasicSingleton) in.readObject();
        }
    }
    public static void main(String[] args) throws Exception{

        // 1. reflection
        // 2. serialization
        BasicSingleton basicSingleton = BasicSingleton.getBasicSingleton();

        basicSingleton.setValue(10);
        String fileName = "singleton.bin";
        saveToFile(basicSingleton, fileName);

        basicSingleton.setValue(20);
        BasicSingleton basicSingleton1 = readFromFile(fileName);
        System.out.println(basicSingleton == basicSingleton1);
        System.out.println(basicSingleton.getValue());
        System.out.println(basicSingleton1.getValue());
    }
}
