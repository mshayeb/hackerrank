import java.io.PrintStream;
import java.util.Arrays;
import java.util.Scanner;

public class Flowers {
	static Scanner in;
	static PrintStream out;
	
	static long flowers(int[] costs, int k) {
		Arrays.sort(costs);
		long total = 0;
		int multiplier = 1;
		for(int i = 0; i < costs.length; i++) {
			total += costs[costs.length - i - 1] * multiplier;
			if(i % k == k - 1) {
				multiplier++;
			}
		}
		return total;
	}

	public static void main(String[] args) {
		in = new Scanner(System.in);
		out = System.out;
		
		int n = in.nextInt();
		int k = in.nextInt();
		int[] ar = new int[n];
		for (int i = 0; i < n; i++) {
			ar[i] = in.nextInt();
		}
		out.println(flowers(ar, k));
	}
}
