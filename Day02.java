import java.io.BufferedReader;
import java.io.FileReader;

public class Day02 {
    public static void main(String[] args) throws Exception {
        int part1 = 0;
        int part2 = 0;
        try (BufferedReader br = new BufferedReader(new FileReader("inputs/day02.txt"))) {
            String line;
            while ((line = br.readLine()) != null && !line.isEmpty()) {
                int opponent = parseHand(line.charAt(0));
                int me = parseHand(line.charAt(2));

                part1 += me;
                if (mod(me - opponent, 3) == 1) {
                    part1 += 6;
                } else if (me == opponent) {
                    part1 += 3;
                }

                if (me == 1) {
                    part2 += mod(opponent - 2, 3) + 1;
                } else if (me == 2) {
                    part2 += opponent + 3;
                } else if (me == 3) {
                    part2 += mod(opponent, 3) + 1;
                    part2 += 6;
                }
            }
        }
        System.out.println(part1);
        System.out.println(part2);
    }

    static int parseHand(char c) {
        if (c == 'A' || c == 'X') {
            return 1;
        } else if (c == 'B' || c == 'Y') {
            return 2;
        } else {
            return 3;
        }
    }

    static int mod(int x, int y) {
        int result = x % y;
        return result < 0 ? result + y : result;
    }
}
