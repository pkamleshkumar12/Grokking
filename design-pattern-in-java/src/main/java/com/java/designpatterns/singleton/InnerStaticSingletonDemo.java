package com.java.designpatterns.singleton;

// It avoids the synchronization problem

class InnerStaticSingleton {

    private InnerStaticSingleton() {
    }

    private static class Impl {
        private static final InnerStaticSingleton INNER_STATIC_SINGLETON = new InnerStaticSingleton();
    }

    public InnerStaticSingleton getInstance() {
        return Impl.INNER_STATIC_SINGLETON;
    }
}

public class InnerStaticSingletonDemo {
}
