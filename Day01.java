import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;

public class Day01 {
    public static void main(String[] args) throws Exception {
        ArrayList<Integer> calories = new ArrayList<>();
        int runningCount = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("inputs/day01.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.isEmpty()) {
                    calories.add(runningCount);
                    runningCount = 0;
                } else {
                    runningCount += Integer.parseInt(line);
                }
            }
        }
        calories.sort(Collections.reverseOrder());
        System.out.println(calories.get(0));
        System.out.println(calories.subList(0, 3).stream().reduce(0, (a, b) -> a + b));
    }
}
