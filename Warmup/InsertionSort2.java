import java.util.*;

public class InsertionSort2 {

	public static void insertionSort(int[] ar) {
		for (int i = 1; i < ar.length; i++) {
			for (int j = i - 1; j >= 0 && ar[j] > ar[j + 1]; j--) {
				swap(ar, j, j + 1);
			}
			printArray(ar);
		}
	}

	static void swap(int[] ar, int i, int j) {
		int tmp = ar[i];
		ar[i] = ar[j];
		ar[j] = tmp;
	}

	/* Tail starts here */
	static void printArray(int[] ar) {
		for (int n : ar) {
			System.out.print(n + " ");
		}
		System.out.println("");
	}

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int[] ar = new int[n];
		for (int i = 0; i < n; i++) {
			ar[i] = in.nextInt();
		}
		insertionSort(ar);
	}
}