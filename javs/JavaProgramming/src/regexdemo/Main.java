package regexdemo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        try {
            var html = new String(Files.readAllBytes(Paths.get("test.html")));
            HTMLTagsFinder.findUnclosedTags(html);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
