package dataStructures;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class HR_Arrays {

  public static void main(String[] args) {



  }

  public static void arraysDS() {
    Scanner reader = new Scanner(System.in);
    int l = Integer.parseInt(reader.nextLine());
    int[] nums = new int[l];
    for (int i = 0; i < l; i++) {
      nums[i] = reader.nextInt();
    }

    for (int i = l - 1; i >= 0; i--) {
      System.out.print(nums[i] + " ");
    }

  }

  public static void leftRotation() {
    Scanner reader = new Scanner(System.in);
    int n = reader.nextInt();
    int d = reader.nextInt();
    Queue<Integer> q = new LinkedList<>();
    for (int i = 0; i < n; i++) {
      q.add(reader.nextInt());
    }
    for (int i = 0; i < d; i++) {
      q.add(q.remove());
    }
    for (int i = 0; i < n; i++) {
      System.out.print(q.remove() + " ");
    }
  }

}
