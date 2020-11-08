package com.java.designpatterns.builder.solution;

import java.util.ArrayList;
import java.util.List;

class Field {
    public String type, name;

    public Field(String type, String name) {
        this.type = type;
        this.name = name;
    }

    @Override
    public String toString() {
        return String.format("public %s %s", type, name);
    }
}

class Class {
    public String name;
    public List<Field> fields = new ArrayList<>();

    public Class() {

    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        String nl = System.lineSeparator();
        sb.append("public class " + name).append(nl)
                .append("{").append(nl);
        for (Field f : fields)
            sb.append("  " + f).append(nl);
        sb.append("}").append(nl);
        return sb.toString();
    }
}

class CodeBuilder {

    private Class theClass = new Class();

    public CodeBuilder(String rootName)
    {
        theClass.name = rootName;
    }

    public CodeBuilder addField(String name, String type)
    {
        theClass.fields.add(new Field(name, type));
        return this;
    }

    @Override
    public String toString() {
        return theClass.toString();
    }
}

public class Solution{

    public static void main(String [] args){
        CodeBuilder cb = new CodeBuilder("Person").addField("name","String")
                .addField("age", "int");
        System.out.println(cb);
    }
}