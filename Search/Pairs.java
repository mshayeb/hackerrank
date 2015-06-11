import java.io.PrintStream;
import java.util.Arrays;
import java.util.Scanner;


public class Pairs {
	static Scanner in;
	static PrintStream out;
	
	static void pairs(int[] ar, int k) {
		Arrays.sort(ar);
		int count = 0;
		for(int i = 0; i < ar.length; i++) {
			for(int j = i + 1; j < ar.length; j++) {
				if(Math.abs(ar[i] - ar[j]) == k) {
					count++;
				} else if(Math.abs(ar[i] - ar[j]) > k) {
					break;
				}
			}
		}
		out.println(count);
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
		pairs(ar, k);
	}
}
