package com.company;

import java.util.ArrayList;
import java.util.Arrays;

public class LinkedListPrac {

    public static ListNode RemoveDuplicate(ListNode head){
        if (head == null | head.next == null)
            return head;
        ListNode temp = head;
        while (temp.next != null){

            if (temp.next.val == temp.val){
                temp.next = temp.next.next;
            }
            else{
                temp = temp.next;
            }
            if (temp == null)
                break;
        }
        return head;
    }

    // https://leetcode.com/problems/partition-list/description/
    public static ListNode partition(ListNode head, int x) {

        if (head == null) return head;
        if (head.next == null) return head;
        ListNode new_head = new ListNode(x-1);
        new_head.next=head;
        ListNode cur = new_head;
        ListNode temp = null;
        ListNode temp_head = null;
        while (cur.next != null){
            if (cur.next.val >= x){
                if (temp == null){
                    temp = cur.next;
                    temp_head = temp;
                }
                else{
                    temp.next = cur.next;
                    temp = temp.next;
                }
                cur.next = cur.next.next;
            }
            else{
                cur = cur.next;
            }
            if (cur == null) break;
        }
        temp.next = null;
        cur.next = temp_head;
        return new_head.next;
    }


    public static ListNode reverseBetween(ListNode head, int m, int n) {
        if (head.next == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode s = dummy;
        ListNode e = dummy;
        int count = 0;
        while (count < n){
            e = e.next;
            if (count < m-1)
                s = s.next;
            count += 1;
        }

        count = n-m;
        while (count > 0){
            ListNode s_next = s.next;
            s.next = s_next.next;
            ListNode e_next = e.next;
            e.next = s_next;
            s_next.next = e_next;
            count -= 1;
        }
        return dummy.next;


    }


    public static void main(String[] args) {
        ListNode head = ListNode.GenLinkedList(new ArrayList<Integer>(Arrays.asList(3,5)));
        // RemoveDuplicate(head).Display();
        // partition(head, 3).Display();
        reverseBetween(head, 1,2).Display();
    }

}
