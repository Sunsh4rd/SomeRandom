package stringdemo;

public class Main {
    public static void main(String[] args) {
        //String pool
        String str1 = "Some sort of text";
        String str2 = "Some sort of text";
        String str3 = new String("Some sort of text");
        System.out.println(str1 == str2); //true
        System.out.println(str1 == str3); //false
        System.out.println(str1.equals(str3)); //true
        StringBuilder builder = new StringBuilder(str1);
        var str4 = str1.replace("o", "i");
        builder.replace(0, 4, "Any");
        System.out.println(builder);
        builder.append("and appended");
        System.out.println(builder);
    }
}
