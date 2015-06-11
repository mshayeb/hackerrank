package problems;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

/*
 * Problem Statement
 * There are N integers in an array A. All but one integer occur in pairs. Your 
 * task is to find out the number that occurs only once.
 *
 * Input Format
 * The first line of the input contains an integer N indicating the number of integers. 
 * The next line contains N space separated integers that form the array A.
 *
 * Constraints
 * 1 <= N < 100 
 * N % 2 = 1 ( N is an odd number ) 
 * 0 <= A[i] <= 100, ∀ i ∈ [1, N]
 * 
 * Output Format
 * Output S, the number that occurs only once.
 */

/**
 *
 * @author Amador Cuenca <sphi02ac@gmail.com>
 */
public class LonelyInteger {
    public static void main(String[] args) throws FileNotFoundException {
        int[] elems = getArrayFromScanner();
        
        System.out.println(lonelyinteger(elems));        
    }
    
    static int lonelyinteger(int[] elems) {       
        for (int i = 0, j = 1; i < elems.length; i = i + 2, j = j + 2) {
            if (j >= elems.length) {
                return elems[i];
            }
        }
        
        return 0;
    }
    
    static int[] getArrayFromScanner() throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("src/testcases/LonelyInteger.txt"));
        int n = scanner.nextInt();
        int[] elems = new int[n];
        
        for (int i = 0; i < n; i++) {
            elems[i] = scanner.nextInt();
        }
        
        Arrays.sort(elems);
        
        return elems;
    }
}
