package com.company;




import java.util.Arrays;

public class MyArrayList{

    private static final int DEFAULT_CAPACITY = 10;

    private int theSize;
    private int[] theItems;

    private void doClear(){
        theSize = 0;
    }


    public MyArrayList(){
        doClear();
        ensureCapacity(DEFAULT_CAPACITY);
    }

    public int size(){
        return theSize;
    }

    public boolean isEmpty(){
        return size()==0;
    }

    public void trim(){
        ensureCapacity(size());
    }

    private void ensureCapacity(int capacity){
        if (capacity < theSize)
            return;

        int[] old = theItems;
        theItems = new int[capacity];
        for (int i = 0; i < size(); i++) {
            theItems[i] = old[i];
        }
    }




    public void show() {
        System.out.println(Arrays.toString(theItems));
        System.out.println(theItems.length);
    }

}
