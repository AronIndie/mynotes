package algorithm;

import java.util.HashMap;

public class FindTwo {

    public static int[] findTwo(int[] input, int value){
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < input.length; i++) {
            map.put(input[i], i);
        }
        int[] result = {-1, -1};
        for (int i = 0; i < input.length; i++) {
            if (input[i] < value) {
                int target = value - input[i];
                if (map.containsKey(target)){
                    result[0] = i;
                    result[1] = map.get(target);
                }


            }
        }
        return result;
    }

    public static void main(String[] args) {
        int[] input = {1,2,3,4};

        int[] result = findTwo(input, 6);
        System.out.println(result[1]);
    }
}
