import java.io.BufferedReader;
import java.io.FileReader;

public class Day03 {
    public static void main(String[] args) throws Exception {
        int part1 = 0;
        int part2 = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("inputs/day03.txt"))) {
            String line;
            int elf = 0;
            boolean[][] badges = new boolean[3][52];
            while ((line = br.readLine()) != null) {
                boolean[] priorities = new boolean[52];
                boolean part1Done = false;
                for (int i = 0; i < line.length(); ++i) {
                    int p = priority(line.charAt(i));
                    badges[elf][p] = true;
                    if (!part1Done) {
                        if (i < line.length() / 2) {
                            priorities[p] = true;
                        } else {
                            if (priorities[p]) {
                                part1 += p + 1;
                                part1Done = true;
                            }
                        }
                    }
                }
                if (elf == 2) {
                    for (int i = 0; i < 52; ++i) {
                        if (badges[0][i] && badges[1][i] && badges[2][i]) {
                            part2 += i + 1;
                            break;
                        }
                    }
                    badges = new boolean[3][52];
                }
                elf = (elf + 1) % 3;
            }
        }
        System.out.println(part1);
        System.out.println(part2);
    }

    static int priority(char c) {
        if (c >= 'a' && c <= 'z')
            return (c - 'a');
        else
            return (c - 'A') + 26;
    }
}
