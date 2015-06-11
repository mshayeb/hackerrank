import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * <p>
 * Solution to the Service Lane <a href="https://www.hackerrank.com/challenges/service-lane">problem</a>
 * </p>
 * 2014
 * 
 * @author Tyrone Hinderson
 */
public class ServiceLane {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        final int cases = Integer.parseInt(reader.readLine().split(" ")[1]);
        final String[] widths = reader.readLine().split(" ");
        for (int i = 0; i < cases; i++) {
            final String[] segs = reader.readLine().split(" ");
            int largestVehicle = 3;
            for (int j = Integer.parseInt(segs[0]); j <= Integer.parseInt(segs[1]) && j < widths.length; j++) {
                final int width = Integer.parseInt(widths[j]);
                if (width < largestVehicle) {
                    largestVehicle = width;
                }
            }
            System.out.println(largestVehicle);
        }
    }
}
