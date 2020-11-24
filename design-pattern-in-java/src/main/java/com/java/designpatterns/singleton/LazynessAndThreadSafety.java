package com.java.designpatterns.singleton;

class LazySingleton {

    private static LazySingleton instance;

    private LazySingleton() {
        System.out.println("initializing a lazy singleton");
    }

    // double check locking
    public static LazySingleton getInstance() {

        if (instance == null) {
            synchronized (LazySingleton.class) {
                if (instance == null) {
                    instance = new LazySingleton();
                }
            }
        }
        return instance;
    }
}


public class LazynessAndThreadSafety {

    public static void main(String[] args) {
        LazySingleton lazySingleton = LazySingleton.getInstance();
    }
}
