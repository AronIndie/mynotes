package com.company;

import javafx.util.Pair;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class SortPrac {

    public static void QuickSortNoRecur(int[] arr){

        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(0,arr.length-1));
        while (!queue.isEmpty()){
            Pair<Integer, Integer> pair = queue.poll();
            int a = pair.getKey();
            int b = pair.getValue();
            if (a >= b)
                continue;
            int start = a;
            int end = b;
            int target = arr[b];
            while (a < b){
                while ((a < b) & (arr[a] <= target))
                    a += 1;
                arr[b] = arr[a];
                while ((a < b) & (arr[b] > target))
                    b -= 1;
                arr[a] = arr[b];
            }
            arr[a] = target;
            Pair<Integer, Integer> left_index = new Pair<>(start, a-1);
            Pair<Integer, Integer> right_index = new Pair<>(a+1, end);
            queue.offer(left_index);
            queue.offer(right_index);
        }


    }


    public static void main(String[] args) {
        int[] a = {1,3,2,4,6,0,9,5};
        QuickSortNoRecur(a);
        System.out.println(Arrays.toString(a));
    }
}
