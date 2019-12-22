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
    //  https://www.hackerrank.com/challenges/array-left-rotation/problem
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

  public static void sparseArrays() {
    // https://www.hackerrank.com/challenges/sparse-arrays/problem
    Scanner reader = new Scanner(System.in);
    int n = reader.nextInt();
    String[] strings = new String[n];
    for (int i = 0; i < n; i++) {
      strings[i] = reader.next();
    }
    int q = reader.nextInt();
    String[] queries = new String[q];
    for (int i = 0; i < q; i++) {
      queries[i] = reader.next();
    }
    reader.close();
    int[] result = new int[q];
    for (int i = 0; i < queries.length; i++) {
      for (int j = 0; j < strings.length; j++) {
        if (queries[i].equals(strings[j])) {
          result[i] += 1;
        }
      }
    }
    for (int i :
        result) {
      System.out.println(i);
    }
  }


}
