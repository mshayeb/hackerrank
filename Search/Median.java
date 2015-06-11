import java.io.PrintStream;
import java.util.Map.Entry;
import java.util.Scanner;
import java.util.TreeMap;

public class Median {
	static Scanner in;
	static PrintStream out;

	// a simple doubly-linked list
	static class LinkedNode {
		long value;
		LinkedNode left, right;

		public LinkedNode(long value) {
			this.value = value;
		}

		public LinkedNode(long value, LinkedNode left, LinkedNode right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}

		public LinkedNode insertLeft(long value) {
			LinkedNode node = new LinkedNode(value, left, this);
			if (left != null) {
				left.right = node;
			}
			left = node;
			return node;
		}

		public LinkedNode insertRight(long value) {
			LinkedNode node = new LinkedNode(value, this, right);
			if (right != null) {
				right.left = node;
			}
			right = node;
			return node;
		}
		
		public void remove() {
			if (left != null) {
				left.right = right;
			}
			if(right != null) {
				right.left = left;
			}
		}

		@Override
		public String toString() {
			return value + ", " + String.valueOf(right);
		}
	}

	static LinkedNode list = null;
	
	// a tree map mapping each value to the last node in the list with its value
	static TreeMap<Long, LinkedNode> index = new TreeMap<>();
	
	// a pointer for the median in the list and a flag indicating if its a single
	// value or an average of two values
	static LinkedNode median = null;
	static boolean singleMedian = true;

	static void add(long value) {
		// if no element present yet, initialize stuff and return
		if (median == null) {
			median = list = new LinkedNode(value);
			index.put(value, median);
			return;
		}
		// find the list node in front of which the new node should be inserted
		Entry<Long, LinkedNode> prevEntry = index.floorEntry(value);
		if (prevEntry != null) {
			LinkedNode newNode = prevEntry.getValue().insertRight(value);
			
			// if it is a new value, add a new entry in the index; if it is
			// an existing value, then the new node is now the last element
			// and must be in the index
			index.put(value, newNode);
		} else {
			// if there is no such node, preprend it to the list
			list = list.insertLeft(value);
			index.put(value, list);
		}
		
		// move median to the left or to the right, if needed
		if(singleMedian && value < median.value) {
			median = median.left;
		} else if(!singleMedian && value >= median.value) {
			median = median.right;
		}
		singleMedian = !singleMedian;
	}
	
	static boolean remove(long value) {
		// find node; if not exists, return false
		LinkedNode node = index.get(value);
		if(node == null) {
			return false;
		}
		// update index: if the node to remove is the only one with
		// its value, remove index entry; else, update it
		if(node.left != null && node.left.value == value) {
			index.put(value, node.left);
		} else {
			index.remove(value);
		}

		// if we are removing the list head, update it before removal
		if(node == list) {
			list = list.right;
		}
		
		// (finally) remove the node from the list
		// the median pointer will be updated later; a removed node does
		// not lose its pointers to its old left and right siblings
		node.remove();
		
		// if the list is empty, put median to null and we're done
		if(list == null) {
			median = null;
			return true;
		}
		
		// move median to the left or to the right, if needed
		if(node == median) {
			median = singleMedian ? median.left : median.right;
		} else if(!singleMedian && value < median.value) {
			median = median.right;
		} else if(singleMedian && value >= median.value) {
			median = median.left;
		}
		singleMedian = !singleMedian;
		return true;
	}
	
	static String getMedian() {
		if(median == null) {
			return "Wrong!";
		}
		if(singleMedian) {
			return "" + median.value;
		}
		long diff = median.right.value - median.value;
		long med = median.value + diff / 2;
		if(diff % 2 == 0) {
			return "" + med;
		}
		if(med == -1) {
			return "-0.5";
		}
		return med >= 0 ? med + ".5": (med + 1) + ".5";
	}

	public static void main(String[] args) {
		in = new Scanner(System.in);
		out = System.out;

		int n = in.nextInt();
		for (int i = 0; i < n; i++) {
			if (in.next().equals("a")) {
				add(in.nextLong());
				out.println(getMedian());
			} else {
				if(remove(in.nextLong())) {
					out.println(getMedian());
				} else {
					out.println("Wrong!");
				}
			}
		}
	}
}
