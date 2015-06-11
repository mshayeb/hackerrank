package problems;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/*
 * Problem Statement
 * You are given N sticks, where each stick is of positive integral length. 
 * A cut operation is performed on the sticks such that all of them are reduced 
 * by the length of the smallest stick.
 * 
 * Suppose we have 6 sticks of length
 * 5 4 4 2 2 8
 * then in one cut operation we make a cut of length 2 from each of the 6 sticks. 
 * For next cut operation 4 sticks are left (of non-zero length), whose length are
 * 3 2 2 6
 * Above step is repeated till no sticks are left.
 * Given length of N sticks, print the number of sticks that are cut in subsequent cut operations.
 *
 * Input Format 
 * The first line contains a single integer N. 
 * The next line contains N integers: a0, a1,...aN-1 separated by space, where 
 * a(i) represents the length of ith stick.
 * 
 * Output Format 
 * For each operation, print the number of sticks that are cut in separate line.

 * Constraints 
 * 1 ≤ N ≤ 1000 
 * 1 ≤ a(i) ≤ 1000
 */

/**
 *
 * @author Amador Cuenca <sphi02ac@gmail.com>
 */
public class CutTheStick {
    public static void main(String[] args) throws FileNotFoundException {
        List<Integer> list = getArrayFromScanner();
        List<Integer> tmpList = new LinkedList<>();
        int inversions;
        
        while (list.size() > 0) {   
            Collections.sort(list);
            int pivot = list.get(0);
            inversions = 0;
            
            for (int i = 0; i < list.size(); i++) {
                int tmp = list.get(i) - pivot;
                
                if (list.get(i) != 0) {
                    if (tmp > 0) {
                        list.set(i, tmp);                    
                        tmpList.add(list.get(i));
                    }
                    
                    inversions++;
                }
            }
                    
            list = tmpList;
            tmpList = new LinkedList<>();
            
            System.out.println(inversions);
        }
    }
    
    private static List<Integer> getArrayFromScanner() throws FileNotFoundException {
        Scanner sc = new Scanner(new File("src/testcases/CutTheStick.txt"));
        
        int n = sc.nextInt();
        List<Integer> list = new LinkedList<>();
        
        for (int i = 0; i < n; i++) {
            list.add(sc.nextInt());
        }
                
        return list;
    }
}
