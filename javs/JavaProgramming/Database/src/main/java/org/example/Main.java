package org.example;

import java.sql.DriverManager;
import java.sql.SQLException;

public class Main {
    public static void main(String[] args) {
        var connectionString = "jdbc:postgresql://ep-weathered-math-909876.us-east-2.aws.neon.tech/apartmentsdb?user=ssoslickk&password=H94xCKgdQjuS";
        try(var conn = DriverManager.getConnection(connectionString)) {
            System.out.println("ok");
        } catch (SQLException e) {
            System.out.println("Connection failed");
        }
    }
}