package graphs;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/**
 * <p>
 * Solution to the "even tree" problem Check out <a href="https://www.hackerrank.com/challenges/even-tree">the
 * challenge</a>
 * </p>
 * <p>
 *
 * </p>
 * 2014
 * 
 * @author Tyrone Hinderson
 */
public class EvenTree {
    public static void main(String[] args) throws Exception {
        BufferedReader stdin = new BufferedReader(new InputStreamReader(System.in));
        String[] counts = stdin.readLine().split(" ");
        int nodes = Integer.parseInt(counts[0]);
        int[] childToParent = new int[nodes + 1];
        int[] nodeTotals = new int[nodes + 1];
        for (int i = 0; i < nodeTotals.length; i++) {
            nodeTotals[i] = 1;
        }

        for (int i = 0; i < Integer.parseInt(counts[1]); i++) {
            String[] edge = stdin.readLine().split(" ");
            childToParent[Integer.parseInt(edge[0])] = Integer.parseInt(edge[1]);
        }

        int edgesToCut = 0;
        for (int i = nodes; i > 1; i--) {
            int nodeTotal = nodeTotals[i];
            if (nodeTotal % 2 == 0)
                edgesToCut++;
            nodeTotals[childToParent[i]] += nodeTotal;
        }
        System.out.println(edgesToCut);
    }
}
