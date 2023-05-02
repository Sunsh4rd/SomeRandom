package regexdemo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Main {
    public static void main(String[] args) {
        var openingTagExpr = "<[a-zA-Z]+[^>]*>";
        try(var html = Files.lines(Paths.get("test.html"))) {
            html.filter(s -> s.matches(openingTagExpr))
                    .forEach(System.out::println);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
