import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Stack;

public class Day05 {
    public static void main(String[] main) throws Exception {

        try (var br = new BufferedReader(new FileReader("inputs/day05.txt"))) {
            String line;
            var chart = new ArrayList<String>();
            int nCols = 0;
            while (!(line = br.readLine()).isEmpty()) {
                if (line.charAt(1) == '1') {
                    line = line.trim();
                    nCols = Integer.parseInt(line.substring(line.length() - 1));
                } else {
                    chart.add(line.replaceAll("\\s+$", ""));
                }
            }
            var part1 = new ArrayList<Stack<Character>>(nCols);
            var part2 = new ArrayList<Stack<Character>>(nCols);
            for (int i = 0; i < nCols; ++i) {
                part1.add(new Stack<>());
                part2.add(new Stack<>());
            }
            Collections.reverse(chart);
            for (String chartLine : chart) {
                int nLineCols = (chartLine.length() + 1) / 4;
                for (int i = 0; i < nLineCols; ++i) {
                    char crate = chartLine.charAt((i * 4) + 1);
                    if (crate != ' ') {
                        part1.get(i).add(crate);
                        part2.get(i).add(crate);
                    }
                }
            }

            while ((line = br.readLine()) != null) {
                String[] tokens = line.split(" ");
                var n = Integer.parseInt(tokens[1]);
                var source1 = part1.get(Integer.parseInt(tokens[3]) - 1);
                var target1 = part1.get(Integer.parseInt(tokens[5]) - 1);
                var source2 = part2.get(Integer.parseInt(tokens[3]) - 1);
                var target2 = part2.get(Integer.parseInt(tokens[5]) - 1);

                for (int i = 0; i < n; ++i) {
                    target2.add(source2.get(source2.size() - n + i));
                }
                for (int i = 0; i < n; ++i) {
                    target1.add(source1.pop());
                    source2.pop();
                }
            }

            for (var stack : part1) {
                System.out.print(stack.get(stack.size() - 1));
            }
            System.out.println();
            for (var stack : part2) {
                System.out.print(stack.get(stack.size() - 1));
            }
            System.out.println();
        }
    }
}
