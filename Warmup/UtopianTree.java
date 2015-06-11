package warmup;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * <p>
 * Solution to the "Utopian Tree" problem. Check out <a href="https://www.hackerrank.com/challenges/utopian-tree">the
 * challenge</a>
 * </p>
 * 2014
 * 
 * @author Tyrone Hinderson
 */
public class UtopianTree {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final int cases = Integer.parseInt(reader.readLine());
        for (int i = 0; i < cases; i++) {
            final int cycles = Integer.parseInt(reader.readLine());
            int height = 1;
            for (int j = 0; j < cycles; j++) {
                if (j % 2 == 0) { // monsoon cycle
                    height *= 2;
                } else { // summer cycle
                    height += 1;
                }
            }
            System.out.println(height);
        }
    }
}
