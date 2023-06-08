package org.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;

public class Main {

    private static Connection connection;

    static {
        var connectionString = "jdbc:postgresql://ep-weathered-math-909876.us-east-2.aws.neon.tech/apartmentsdb?user=ssoslickk&password=H94xCKgdQjuS";
        try {
            connection = DriverManager.getConnection(connectionString);
            System.out.println("ok");
        } catch (SQLException e) {
            System.out.println("Connection failed");
        }
    }

    public static void main(String[] args) {
        try {
            var stmtApartments = connection.createStatement();
            var sqlApartments = "CREATE TABLE IF NOT EXISTS apartment (" +
                    "id serial primary key," +
                    "street_name varchar(50)," +
                    "building_number int," +
                    "apartment_number int," +
                    "overall_space int," +
                    "living_space int," +
                    "number_of_rooms int," +
                    "floor int," +
                    "has_elevator boolean," +
                    "has_concierge boolean," +
                    "has_private_area boolean," +
                    "has_parking_lot boolean" +
                    ");";
            stmtApartments.execute(sqlApartments);

            var stmtResidents = connection.createStatement();
            var sqlResidents = "CREATE TABLE IF NOT EXISTS resident (" +
                    "id serial primary key," +
                    "first_name varchar(50)," +
                    "last_name varchar(50)," +
                    "birth_date date," +
                    "gender varchar(2)," +
                    "apartment_id int," +
                    "FOREIGN KEY (apartment_id) REFERENCES apartment (id)" +
                    ");";
            stmtResidents.execute(sqlResidents);

            var stmtPreviousOwners = connection.createStatement();
            var sqlPreviousOwners = "CREATE TABLE IF NOT EXISTS previous_owner (" +
                    "apartment_id int," +
                    "resident_id int," +
                    "PRIMARY KEY (apartment_id, resident_id)," +
                    "FOREIGN KEY (apartment_id) REFERENCES apartment (id)," +
                    "FOREIGN KEY (resident_id) REFERENCES resident (id)" +
                    ");";
            stmtPreviousOwners.execute(sqlPreviousOwners);

//            var deleteApts = connection.createStatement();
//            var sqldeleteApts = "DELETE FROM \"apartment\"";
//            deleteApts.execute(sqldeleteApts);
//
//            var stmtInsertApartment = connection.createStatement();
//            var sqlInsertApartment = "INSERT INTO apartment (street_name," +
//                    "building_number," +
//                    "apartment_number," +
//                    "overall_space," +
//                    "living_space," +
//                    "number_of_rooms," +
//                    "floor," +
//                    "has_elevator," +
//                    "has_concierge," +
//                    "has_private_area," +
//                    "has_parking_lot) " +
//                    "VALUES ('1-я улица', 1, 20, 80, 80, 4, 6, true, true, true, true), " +
//                    "('2-я улица', 2, 20, 60, 60, 3, 6, true, false, true, false), " +
//                    "('2-я улица', 1, 21, 60, 60, 3, 2, true, false, true, false), " +
//                    "('1-я улица', 2, 22, 70, 60, 3, 4, true, false, true, false), " +
//                    "('3-я улица', 3, 21, 60, 60, 3, 6, true, false, true, false), " +
//                    "('4-я улица', 5, 22, 40, 40, 2, 5, false, false, false, false), " +
//                    "('4-я улица', 1, 25, 80, 70, 4, 3, true, true, true, true), " +
//                    "('3-я улица', 1, 25, 60, 60, 3, 6, true, false, true, false), " +
//                    "('5-я улица', 2, 25, 60, 60, 3, 6, true, false, true, false), " +
//                    "('5-я улица', 3, 21, 60, 60, 3, 6, true, false, true, false), " +
//                    "('6-я улица', 2, 22, 60, 60, 3, 6, true, false, true, false), " +
//                    "('6-я улица', 2, 23, 60, 60, 3, 6, true, false, true, false)";
//            stmtInsertApartment.execute(sqlInsertApartment);

//            var stmtInsertResident = connection.createStatement();
//            var sqlInsertResident = "INSERT INTO resident (" +
//                    "first_name," +
//                    "last_name," +
//                    "birth_date," +
//                    "gender," +
//                    "apartment_id) " +
//                    "VALUES ('Иван', 'Иванов', '1990-01-01', 'M', 2), " +
//                    "('Петр', 'Петров', '1991-02-02', 'M', 3), " +
//                    "('Жанна', 'Дарк', '1995-03-03', 'F', 4), " +
//                    "('Вася', 'Пупкин', '2007-01-01', 'M', 5), " +
//                    "('Вернон', 'Роше', '2008-01-01', 'M', 6), " +
//                    "('Алена', 'Солнышко', '2000-07-27', 'F', 7), " +
//                    "('Йозеф', 'Швейк', '1950-05-05', 'M', 8), " +
//                    "('Индржих', 'Лукаш', '1950-04-04', 'M', 8), " +
//                    "('Райан', 'Гослинг', '1993-03-03', 'M', 9), " +
//                    "('Анна', 'Каренина', '1960-01-01', 'F', 10), " +
//                    "('Эредин', 'Гласс', '1992-02-02', 'M', 11), " +
//                    "('Аксель', 'Эспарза', '1998-08-08', 'M', 12), " +
//                    "('Абрам', 'Козырев', '1989-09-09', 'M', 13)";
//            stmtInsertResident.execute(sqlInsertResident);

//            var stmtInsertPreviousOwner = connection.createStatement();
//            var sqlInsertPreviousOwner = "INSERT INTO previous_owner (" +
//                    "apartment_id," +
//                    "resident_id) " +
//                    "VALUES (2, 2), " +
//                    "(2, 12), " +
//                    "(3, 3), " +
//                    "(3, 11), " +
//                    "(4, 4), " +
//                    "(4, 10), " +
//                    "(5, 5), " +
//                    "(5, 9), " +
//                    "(6, 6), " +
//                    "(6, 8), " +
//                    "(7, 7)";
//            stmtInsertPreviousOwner.execute(sqlInsertPreviousOwner);
//            System.out.println("Квартиры и люди, которые в них живут:");
//            var sql1 = "select a.id as a_id, street_name, building_number, apartment_number, r.id as r_id, first_name, last_name, apartment_id from apartment a\n" +
//                    "join resident r\n" +
//                    "on a.id = apartment_id";
//            var stmt1 = connection.prepareStatement(sql1);
//            var rs = stmt1.executeQuery();
//            while (rs.next()) {
//                System.out.println(rs.getString("street_name"));
//                System.out.println(rs.getInt("building_number"));
//                System.out.println(rs.getInt("apartment_number"));
//                System.out.println(rs.getString("first_name"));
//                System.out.println(rs.getString("last_name"));
//                System.out.println("-----------------------------------------");
//            }
//            System.out.println("*******************************************");
//
//            System.out.println("Прошлые хозяева некоторой квартиры:");
//            var sql2 = "select r.id as r_id, first_name, last_name, p.apartment_id as p_aid from resident r\n" +
//                    "join previous_owner p\n" +
//                    "on p.resident_id = r.id";
//            var stmt2 = connection.prepareStatement(sql2);
//            var rs2 = stmt2.executeQuery();
//            while (rs2.next()) {
//                System.out.println(rs2.getString("first_name"));
//                System.out.println(rs2.getString("last_name"));
//                System.out.println(rs2.getInt("p_aid"));
//                System.out.println("-----------------------------------------");
//            }
//            System.out.println("*******************************************");
//
//            System.out.println("Для военкомата (адреса людей для армии):");
//            var sql3 = "select a.id as a_id, street_name, building_number, apartment_number, r.id as r_id, first_name, last_name, birth_date, gender, apartment_id from apartment a\n" +
//                    "join resident r\n" +
//                    "on a.id = apartment_id\n" +
//                    "where gender = 'M' and DATE_PART('year', CURRENT_DATE) - DATE_PART('year', birth_date) >= 18 and DATE_PART('year', CURRENT_DATE) - DATE_PART('year', birth_date) <= 50";
//            var stmt3 = connection.prepareStatement(sql3);
//            var rs3 = stmt3.executeQuery();
//            while (rs3.next()) {
//                System.out.println(rs3.getString("first_name"));
//                System.out.println(rs3.getString("last_name"));
//                System.out.println(rs3.getString("street_name"));
//                System.out.println(rs3.getInt("building_number"));
//                System.out.println(rs3.getInt("apartment_number"));
//                System.out.println("-----------------------------------------");
//            }
//            System.out.println("*******************************************");

//            System.out.println("Сортировка по площадям:");
//            var sql4 = "select a.id as a_id, street_name, building_number, apartment_number, overall_space from apartment a\n" +
//                    "order by overall_space";
//            var stmt4 = connection.prepareStatement(sql4);
//            var rs4 = stmt4.executeQuery();
//            while (rs4.next()) {
//                System.out.println(rs4.getInt("a_id"));
//                System.out.println(rs4.getString("street_name"));
//                System.out.println(rs4.getInt("building_number"));
//                System.out.println(rs4.getInt("apartment_number"));
//                System.out.println(rs4.getInt("overall_space"));
//                System.out.println("-----------------------------------------");
//            }
//            System.out.println("*******************************************");

            System.out.println("Квартиры с 4 комнатами:");
            var sql5 = "select a.id as a_id, street_name, building_number, apartment_number from apartment a\n" +
                    "where number_of_rooms = 4";
            var stmt5 = connection.prepareStatement(sql5);
            var rs5 = stmt5.executeQuery();
            while (rs5.next()) {
                System.out.println(rs5.getInt("a_id"));
                System.out.println(rs5.getString("street_name"));
                System.out.println(rs5.getInt("building_number"));
                System.out.println(rs5.getInt("apartment_number"));
//                System.out.println(rs4.getInt("number_of_rooms"));
                System.out.println("-----------------------------------------");
            }
            System.out.println("*******************************************");
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
