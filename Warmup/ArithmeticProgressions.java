import java.io.PrintStream;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class ArithmeticProgressions {
	static Scanner in;
	static PrintStream out;

	static Node seqTree;

	static int MOD = 1000003;

	static class Node {
		// the indices of the first and last sequence in this subtree
		int st, end;

		// the product of the raw terms (d), the sum of degrees (p) and the
		// product of effective terms (d^p) of the sequences in this subtree
		long rawTerm, degree, term;

		// counter of degrees added recently through update operations and
		// implied term multiplier. The remaining fields of this node already
		// include these values; the children's fields, however, do not
		long addedDegree = 0, addedTerm = 1;

		// left and right branches
		Node left, right;

		// create a leaf node with a single sequence
		public Node(int idx, long d, long p) {
			this.st = this.end = idx;
			this.rawTerm = d;
			this.degree = p;
			term = modPow(d, p);
		}

		// create an internal node with the given children
		private Node(Node left, Node right) {
			this.st = left.st;
			this.end = right.end;
			this.rawTerm = left.rawTerm * right.rawTerm % MOD;
			this.degree = left.degree + right.degree;
			this.term = left.term * right.term % MOD;
			this.left = left;
			this.right = right;
		}

		// updates a node, incrementing the degree of the nodes in the range
		// [st, end] by v. When this call returns, the degree and term fields
		// of this node will have the correct values. The fields of child nodes,
		// however, are not guaranteed to be updated
		void update(int st, int end, long v) {
			if (st > this.end || end < this.st) {
				return;
			}
			// if the operation affects all subtree...
			else if (st <= this.st && end >= this.end) {
				// multiplying the current term with rawTerm ^ v gives the term
				// after the degree update
				long termUpdate = modPow(rawTerm, v);
				degree += v * (this.end - this.st + 1);
				term = term * termUpdate % MOD;

				// if not a leaf node, update addedDegree and addedTerm fields,
				// postponing children update
				if (this.st < this.end) {
					addedDegree += v;
					addedTerm = addedTerm * termUpdate % MOD;
				}
			}
			// else, the operation affects only part of this subtree
			else {
				// propagate update down and update term and degree fields of
				// this node
				left.update(st, end, v);
				right.update(st, end, v);
				degree = left.degree + right.degree + addedDegree
						* (this.end - this.st + 1);
				term = left.term * right.term % MOD * addedTerm % MOD;
			}
		}

		long getTerm(int st, int end) {
			if (st > this.end || end < this.st) {
				return 1;
			} else if (st <= this.st && end >= this.end) {
				return term;
			}
			if (addedDegree > 0) {
				propagateUpdateDown();
			}
			return left.getTerm(st, end) * right.getTerm(st, end) % MOD;
		}

		long getDegree(int st, int end) {
			if (st > this.end || end < this.st) {
				return 0;
			} else if (st <= this.st && end >= this.end) {
				return degree;
			}
			if (addedDegree > 0) {
				propagateUpdateDown();
			}
			return left.getDegree(st, end) + right.getDegree(st, end);
		}

		private void propagateUpdateDown() {
			left.update(this.st, this.end, addedDegree);
			right.update(this.st, this.end, addedDegree);
			addedDegree = 0;
			addedTerm = 1;
		}

		@Override
		public String toString() {
			return "Node [st=" + st + ", end=" + end + ", term=" + term
					+ ", degree=" + degree + "(+" + addedDegree + ")"
					+ ", left=" + left + ", right=" + right + "]";
		}

		static Node build(long[] degrees, long[] rawTerms) {
			Queue<Node> currLayer = new LinkedList<>();
			for (int i = 0; i < rawTerms.length; i++) {
				currLayer.add(new Node(i, rawTerms[i], degrees[i]));
			}
			while (currLayer.size() != 1) {
				Queue<Node> nextLayer = new LinkedList<>();
				while (!currLayer.isEmpty()) {
					Node left = currLayer.poll();
					if (currLayer.isEmpty()) {
						nextLayer.add(left);
						break;
					}
					Node right = currLayer.poll();
					nextLayer.add(new Node(left, right));
				}
				currLayer = nextLayer;
			}
			return currLayer.poll();
		}
	}

	static void query(int st, int end) {
		long degree = seqTree.getDegree(st, end);
		long term = seqTree.getTerm(st, end);
		term = term * modFact(degree) % MOD;
		out.println(degree + " " + term);
	}

	static void update(int st, int end, int v) {
		seqTree.update(st, end, v);
	}

	static long[] factMem = new long[MOD];
	static {
		factMem[0] = factMem[1] = 1;
	}
	static int nextFact = 2;
	
	static long modFact(long n) {
		if(n >= MOD) {
			return 0;
		}
		while (n >= nextFact) {
			factMem[nextFact] = nextFact * factMem[nextFact - 1] % MOD;
			nextFact++;
		}
		return factMem[(int) n];
	}

	static long modPow(long a, long b) {
		if (b == 0) {
			return 1;
		}
		if (b == 1) {
			return a;
		}
		long halfPow = modPow(a, b / 2);
		long pow = halfPow * halfPow % MOD;
		return b % 2 == 0 ? pow : pow * a % MOD;
	}

	public static void main(String[] args) {
		in = new Scanner(System.in);
		out = System.out;

		int n = in.nextInt();
		long[] term = new long[n];
		long[] degree = new long[n];

		for (int i = 0; i < n; i++) {
			in.nextInt();
			term[i] = in.nextInt();
			degree[i] = in.nextInt();
		}
		seqTree = Node.build(degree, term);

		int q = in.nextInt();
		for (int i = 0; i < q; i++) {
			if (in.nextInt() == 0) {
				query(in.nextInt() - 1, in.nextInt() - 1);
			} else {
				update(in.nextInt() - 1, in.nextInt() - 1, in.nextInt());
			}
		}
	}
}
