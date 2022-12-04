import java.io.BufferedReader;
import java.io.FileReader;
import java.util.stream.Stream;

public class Day04 {
    public static void main(String[] args) throws Exception {
        int part1 = 0;
        int part2 = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("inputs/day04.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] vals = line.split("[-,]");
                Integer[] sections = Stream.of(vals).map(Integer::valueOf).toArray(Integer[]::new);
                int lo1 = sections[0], hi1 = sections[1], lo2 = sections[2], hi2 = sections[3];
                if (lo1 <= lo2 && hi1 >= hi2 || lo2 <= lo1 && hi2 >= hi1) {
                    ++part1;
                }
                if (lo2 <= hi1 && lo2 >= lo1 || lo1 <= hi2 && lo1 >= lo2) {
                    ++part2;
                }
            }
        }
        System.out.println(part1);
        System.out.println(part2);
    }
}
