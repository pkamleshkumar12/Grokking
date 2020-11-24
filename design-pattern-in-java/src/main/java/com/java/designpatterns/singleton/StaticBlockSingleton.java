package com.java.designpatterns.singleton;
// If you are constructing singleton object by using the constructor, throwing exception from constructor will cause trouble
// to avoid such problem use static block

import java.io.File;
import java.io.IOException;

public class StaticBlockSingleton {

    private StaticBlockSingleton() throws IOException {
        System.out.println("Singleton is initializing");
        File.createTempFile(".", ".");
    }

    private static StaticBlockSingleton instance;

    static {
        try {
            instance = new StaticBlockSingleton();
        } catch (IOException e) {
            System.err.println("failed to create singleton: " + e.getMessage());
        }
    }

    public static StaticBlockSingleton getInstance() {
        return instance;
    }
}
