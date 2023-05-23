package regexdemo;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Map;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        var openingTags = new ArrayList<String>();
        var closingTags = new ArrayList<String>();
        var openingTagExpr = Pattern.compile("<(\\w+)[^>]*>");
        var closingTagExpr = Pattern.compile("</(\\w+)>");
        try {
            var html = Files.readString(Paths.get("test.html"));
            System.out.println(html);
            var matcherOpening = openingTagExpr.matcher(html);
            var matcherClosing = closingTagExpr.matcher(html);
            while (matcherOpening.find()) {
                openingTags.add(matcherOpening.group(1));
            }
            while (matcherClosing.find()) {
                closingTags.add(matcherClosing.group(1));
            }
            openingTags.sort(String::compareTo);
            closingTags.sort(String::compareTo);
            for (String tag: closingTags) {
                openingTags.remove(tag);
            }
            System.out.println("Незакрытые теги:");
            Map<String, Long> unclosedTagsCount = openingTags.stream()
                    .collect(Collectors.groupingBy(t -> t, Collectors.counting()));
            System.out.println(unclosedTagsCount);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
