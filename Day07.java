import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Day07 {
    static class File {
        HashMap<String, File> files = null;
        Integer fileSize = null;
        File parent = null;

        File() {
            files = new HashMap<>();
        }

        File(Integer fileSize) {
            this.fileSize = fileSize;
        }

        File cd(String dir) {
            if (dir.equals("..")) {
                return parent;
            } else {
                return files.get(dir);
            }
        }

        void touch(String name, int fileSize) {
            files.put(name, new File(fileSize));
        }

        void mkdir(String name) {
            File dir = new File();
            dir.parent = this;
            files.put(name, dir);
        }
    }

    static int traverse(File cwd, ArrayList<Integer> sizes) {
        if (cwd.fileSize != null) {
            // Is file
            return cwd.fileSize;
        } else {
            // Is directory
            int runningSum = 0;
            for (var entry : cwd.files.values()) {
                int dirSize = traverse(entry, sizes);
                runningSum += dirSize;
            }
            sizes.add(runningSum);
            return runningSum;
        }
    }

    public static void main(String[] args) throws Exception {
        File root = new File();
        File cwd = root;

        try (var br = new BufferedReader(new FileReader("inputs/day07.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] tokens = line.split(" ");
                switch (tokens[0]) {
                    case "$" -> {
                        if (tokens[1].equals("cd") && !tokens[2].equals("/")) {
                            cwd = cwd.cd(tokens[2]);
                        }
                    }
                    case "dir" -> {
                        cwd.mkdir(tokens[1]);
                    }
                    default -> {
                        int fileSize = Integer.parseInt(tokens[0]);
                        cwd.touch(tokens[1], fileSize);
                    }
                }
            }
        }

        ArrayList<Integer> sizes = new ArrayList<>();
        var diskUsed = traverse(root, sizes);
        var part1 = sizes.stream().filter(x -> x <= 100000).reduce(Math::addExact).get();
        System.out.println(part1);

        int usused = 70000000 - diskUsed;
        int needFree = 30000000 - usused;
        Collections.sort(sizes);
        int toDelIdx = Collections.binarySearch(sizes, needFree);
        if (toDelIdx < 0) {
            toDelIdx = -(toDelIdx + 1);
        }
        System.out.println(sizes.get(toDelIdx));
    }
}
