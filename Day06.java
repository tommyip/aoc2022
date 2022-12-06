import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Day06 {
    public static void main(String[] args) throws Exception {
        try (var br = new BufferedReader(new FileReader("inputs/day06.txt"))) {
            String line = br.readLine();
            Deque<Integer> q = new ArrayDeque<>();
            int distinctLength = 14; // part1 = 4, part2 = 14
            for (int i = 0; i < line.length(); ++i) {
                int c = (int) line.charAt(i) - (int) 'a';
                q.add(c);
                if (q.size() > distinctLength) {
                    q.remove();
                }
                if (i >= distinctLength) {
                    boolean[] dup = new boolean[26];
                    boolean dupped = false;
                    for (int qc : q) {
                        if (dup[qc]) {
                            dupped = true;
                        }
                        dup[qc] = true;
                    }
                    if (!dupped) {
                        System.out.println(i + 1);
                        break;
                    }
                }
            }
        }
    }
}
