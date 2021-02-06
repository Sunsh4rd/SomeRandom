// Old good Hello World in Java:
// https://docs.oracle.com/javase/tutorial/getStarted/application/index.html
package HelloWorld;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
 
public class HelloWorld {
  public static void main(final String[] args) {
    final DateTimeFormatter dtf = DateTimeFormatter.ofPattern("h:mm:ss a 'on' MMMM d, yyyy'.'");
    final LocalDateTime now = LocalDateTime.now();
    System.out.println("Hello, World! The current time is " + dtf.format(now));
  }
}