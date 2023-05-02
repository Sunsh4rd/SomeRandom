package regexdemo;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.regex.Pattern;

public class HTMLTagsFinder {
    public static void findUnclosedTags(String html) {
        var openingTagExpr = "<[a-zA-Z]+[^>]*>";
        var closingTagExpr = "</[a-zA-Z]+>";
        var openingTagPattern = Pattern.compile(openingTagExpr);
        var closingTagPattern = Pattern.compile(closingTagExpr);
        var list = new ArrayList<String>();
        System.out.println(html);
        var splitHTML = html.split("\n");
        System.out.println(Arrays.toString(splitHTML));
//        for (String line: html.split("\n")) {
//            System.out.println(line);
//            if (openingTagPattern.matcher(line).matches()) {
//                list.add(line);
//            }
//        }
//        System.out.println(list);
    }
}
