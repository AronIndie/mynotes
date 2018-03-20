package algorithm;

import java.util.Stack;

public class stack2queue {

    private Stack<Integer> stack1 = new Stack<Integer>();
    private Stack<Integer> stack2 = new Stack<Integer>();

    public void push(int i){
        stack1.push(1);
    }

    public int pop(){
        while (!stack1.empty())
            stack2.push(stack1.pop());
        int res = stack2.pop();
        while (!stack2.empty())
            stack1.push(stack2.pop());
        return res;
    }

    public static void main(String[] args) {

    }

}
