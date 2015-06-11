import java.io.PrintStream;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class XorKey {
    static Scanner in;
    static PrintStream out;

    public static final int MAX_BITS = 15;

    static int ceiling(List<Integer> list, int v) {
        int idx = Collections.binarySearch(list, v);
        if (idx < 0)
            idx = -idx - 1;
        return idx >= list.size() ? -1 : idx;
    }

    static class Node {
        int bit = MAX_BITS - 1;
        Node clearBit;
        Node setBit;
        List<Integer> indices = new ArrayList<>();

        Node clearNode() {
            if (clearBit == null) {
                clearBit = new Node();
                clearBit.bit = bit - 1;
            }
            return clearBit;
        }

        Node setNode() {
            if (setBit == null) {
                setBit = new Node();
                setBit.bit = bit - 1;
            }
            return setBit;
        }

        void add(int idx, int x) {
            indices.add(idx);
            if (bit >= 0) {
                Node child = (x & (1 << bit)) == 0 ? clearNode() : setNode();
                child.add(idx, x);
            }
        }

        Node fastForward(int a, int score) {
            if (bit < 0 || (score & (1 << bit)) == 0)
                return this;
            return ((a & (1 << bit)) == 0 ? setBit : clearBit).fastForward(a,
                    score);
        }

        int query(int[] xs, int a, int p, int q) {
            if (bit < 0) {
                return a ^ xs[indices.get(ceiling(indices, p))];
            }
            Node goodChild = (a & (1 << bit)) == 0 ? setBit : clearBit;
            if (goodChild != null) {
                int goodIdx = ceiling(goodChild.indices, p);
                if (goodIdx != -1 && goodChild.indices.get(goodIdx) <= q) {
                    int goodValue = xs[goodChild.indices.get(goodIdx)];
                    return goodChild.fastForward(a, a ^ goodValue).query(xs, a, p, q);
                    // return goodChild.query(xs, a, p, q);
                }
            }
            Node badChild = goodChild == setBit ? clearBit : setBit;
            return badChild.query(xs, a, p, q);
        }
    }

    public static void main(String[] args) {
        in = new Scanner(System.in);
        out = System.out;

        int t = in.nextInt();
        for (int i = 0; i < t; i++) {
            int n = in.nextInt();
            int q = in.nextInt();

            int[] xs = new int[n];
            Node tree = new Node();
            for (int j = 0; j < n; j++) {
                int x = in.nextInt();
                xs[j] = x;
                tree.add(j, x);
            }

            for (int j = 0; j < q; j++) {
                int a = in.nextInt();
                int pq = in.nextInt() - 1;
                int qq = in.nextInt() - 1;
                out.println(tree.query(xs, a, pq, qq));
            }
        }
    }
}
