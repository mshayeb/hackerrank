package problems;


import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

/*
 * Problem Statement
 * Shashank likes strings in which consecutive characters are different. 
 * For example, he likes ABABA, while he doesn't like ABAA. Given a string 
 * containing characters A and B only, he wants to change it into a string 
 * he likes. To do this, he is allowed to delete the characters in the string.

 * Your task is to find the minimum number of required deletions.

 * Input Format 
 * The first line contains an integer T i.e. the number of test cases. 
 * Next T lines contain a string each.

 * Output Format 
 * For each test case, print the minimum number of deletions required.

 * Constraints
 * 1 ≤ T ≤ 10 
 * 1 ≤ lengthofString ≤ 10^5 
 */

/**
 *
 * @author Amador Cuenca <sphi02ac@gmail.com>
 */
public class AlternatingCharacters {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("src/testcases/AlternatingCharacters.txt"));
        
        int n = scanner.nextInt();
        
        for (int i = 0; i < n; i++) {
            System.out.println(alternate(scanner.next()));
        }
    }
    
    static int alternate(String row) {
        String[] elems = row.split("");
        String pivot = elems[0];
        int deletions = 0;
        
        for (int i = 1; i < elems.length; i++) {
            if (elems[i].equals(pivot)) {
                deletions++;                
            }
            pivot = elems[i];
        }
        
        return deletions;
    }
}
