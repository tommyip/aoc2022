import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Collections;
import java.util.Iterator;
import java.util.Vector;

public class Day01 {
    public static void main(String[] args) throws Exception {
        Vector<Integer> calories = new Vector<>();
        int runningCount = 0;
        Iterator<String> lines = Files.lines(Path.of("inputs/day01.txt")).iterator();
        while (lines.hasNext()) {
            String line = lines.next().trim();
            if (line.isEmpty()) {
                calories.add(runningCount);
                runningCount = 0;
            } else {
                runningCount += Integer.parseInt(line);
            }
        }
        Collections.sort(calories, Collections.reverseOrder());
        System.out.println(calories.get(0));
        System.out.println(calories.subList(0, 3).stream().reduce(0, (a, b) -> a + b));
    }
}
