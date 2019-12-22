package dataStructures;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class HR_Arrays {

  public static void main(String[] args) {
    arraysDS();


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

}
