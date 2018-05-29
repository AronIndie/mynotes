package com.company;


public class Main {

    public static void main(String[] args) {
        // write your code here
        Solution s = new Solution();
        test1(s);
        System.out.println(2.0 - 1);

    }

    private static void test1(Solution s){
        int target = 10;
        int[][] mat = {{1,2,3}, {4,5,10}, {7,9,12}};
        boolean res = s.Find(target, mat);
        System.out.printf(String.valueOf(res));
    }
}
