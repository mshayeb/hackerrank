package warmup;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * <p>
 * Solution to the "Filling Jars" <a href="https://www.hackerrank.com/challenges/filling-jars">problem</a>
 * </p>
 * 2014
 * 
 * @author Tyrone Hinderson
 */
public class FillingJars {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final String[] nm = reader.readLine().split(" ");
        final int jars = Integer.parseInt(nm[0]);
        final int cases = Integer.parseInt(nm[1]);
        long total = 0;
        for(int i = 0; i < cases; i++){
            final String[] argz = reader.readLine().split(" ");
            final long a = Long.parseLong(argz[0]);
            final long b = Long.parseLong(argz[1]);
            final long k = Long.parseLong(argz[2]);
            total += (b - a + 1) * k;
        }
        System.out.println(total / jars);
    }
}
