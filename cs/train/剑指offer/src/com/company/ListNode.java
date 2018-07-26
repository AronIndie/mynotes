package com.company;

import java.util.ArrayList;
import java.util.Arrays;

public class ListNode {
    public int val;
    public ListNode next = null;
    public ListNode(int val, ListNode next){
        this.val = val;
        this.next = next;
    }

    public ListNode(int val){
        this.val = val;
        this.next = null;
    }

    public void Display(){
        System.out.println(this.val);
        ListNode n = this.next;
        while (n != null){
            System.out.println(n.val);
            n = n.next;
        }
    }


    public static ListNode GenLinkedList(ArrayList<Integer> list){
        ArrayList<ListNode> node_list = new ArrayList<>();
        for (int i = 0; i < list.size(); i++) {
            ListNode temp_node = new ListNode(list.get(i));
            node_list.add(temp_node);
        }
        for (int i = 0; i < node_list.size()-1; i++) {
            node_list.get(i).next = node_list.get(i+1);
        }
        return node_list.get(0);
    }

    public static void main(String[] args) {
        ListNode node1 = new ListNode(10);
        node1.next = new ListNode(20);
        ArrayList<Integer> arr = new ArrayList<Integer>(Arrays.asList(1,2,3,4,2,3));
        ListNode.GenLinkedList(arr).Display();
    }
}
