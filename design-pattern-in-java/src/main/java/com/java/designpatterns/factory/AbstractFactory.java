package com.java.designpatterns.factory;

import org.javatuples.Pair;
import org.reflections.Reflections;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.InvocationTargetException;
import java.rmi.server.ExportException;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.List;
import java.util.Set;

interface HotDrink {
    void consume();
}

class Tea implements HotDrink {

    @Override
    public void consume() {
        System.out.println("The tea is delicious");
    }
}

class Coffee implements HotDrink {

    @Override
    public void consume() {
        System.out.println("This Coffee is delicious");
    }
}

interface HotDrinkFactory {

    HotDrink prepare(int amount);
}

class TeaFactory implements HotDrinkFactory {

    @Override
    public HotDrink prepare(int amount) {
        System.out.println("preparing tea for amount:" + amount);
        return new Tea();
    }
}

class CoffeeFactory implements HotDrinkFactory {

    @Override
    public HotDrink prepare(int amount) {
        System.out.println("preparing Coffee for amount:" + amount);
        return new Coffee();
    }
}

class HotDrinkMachine {

    private List<Pair<String, HotDrinkFactory>> namedFactories = new ArrayList<>();

    public HotDrinkMachine() throws Exception {
        Set<Class<? extends HotDrinkFactory>> types =
                new Reflections("")
                        .getSubTypesOf(HotDrinkFactory.class);
        for (Class<? extends HotDrinkFactory> type : types) {
            namedFactories.add(new Pair<>(
                    type.getSimpleName().replace("Factory", ""),
                    type.getDeclaredConstructor().newInstance()));
        }
    }

    public HotDrink makeDrink() throws Exception {

        System.out.println("Available Drinks");
        for (int index = 0; index < namedFactories.size(); ++index) {
            Pair<String, HotDrinkFactory> item = namedFactories.get(index);
            System.out.println("" + index + ": " + item.getValue0());
        }
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s;
            int i, amount;
            if ((s = reader.readLine()) != null
                    && (i = Integer.parseInt(s)) >= 0
                    && i < namedFactories.size()) {
                System.out.println("specify amount:");
                s = reader.readLine();
                if (s != null && (amount = Integer.parseInt(s)) > 0) {
                     return namedFactories.get(i).getValue1().prepare(amount);
                }
                System.out.println("Incorrect input, try again!!");
            }
        }
    }

}

public class AbstractFactory {
    public static void main(String[] args) throws Exception {

        HotDrinkMachine machine = new HotDrinkMachine();
        HotDrink drink = machine.makeDrink();
        drink.consume();
    }
}
