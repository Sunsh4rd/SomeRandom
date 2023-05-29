package collectionsdemo;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        List<String> stringList = new LinkedList<>(); //Связный список
        List<String> stringList1 = new ArrayList<>(); //В основе массив

        stringList.add("kefteme");
        stringList1.add("kefteme");
        stringList.add("aboba");
        stringList1.add("aboba");
        stringList.add(1, "booba");
        stringList1.add(1, "booba");
        stringList.sort(Comparator.comparing(String::toString));
        System.out.println(stringList);
        System.out.println(stringList1);
        List<String> ofMethod = List.of(
                "aboba",
                "booba",
                "kefteme"
        );

        System.out.println(ofMethod);
        try {
            ofMethod.add("newstr");
            System.out.println(ofMethod);
        }
        catch (UnsupportedOperationException e) {
            System.out.println("can't modify Lis.of");
        }

        Map<MapKey, String> map = new HashMap<>();
        map.put(new MapKey("thiskey"), "value4");
        map.put(new MapKey("key"), "value1");
        map.put(new MapKey("anotherkey"), "value3");
        map.put(new MapKey("keyaaa"), "value2");

        Map<MapKey, String> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put(new MapKey("thiskey"), "value4");
        linkedHashMap.put(new MapKey("key"), "value1");
        linkedHashMap.put(new MapKey("anotherkey"), "value3");
        linkedHashMap.put(new MapKey("keyaaa"), "value2");

        Map<MapKey, String> treeMap = new TreeMap<>(Comparator.comparingInt(o -> o.value().length()));
        treeMap.put(new MapKey("thiskey"), "value4");
        treeMap.put(new MapKey("key"), "value1");
        treeMap.put(new MapKey("anotherkey"), "value3");
        treeMap.put(new MapKey("keyaaa"), "value2");


        System.out.println(map);
        System.out.println(linkedHashMap);
        System.out.println(treeMap);

        Set<String> stringSet = new HashSet<>(stringList);
        Set<String> stringSet1 = new TreeSet<>(Comparator.comparing(String::length));
        System.out.println(stringSet);
        stringSet.add("aboba");
        stringSet.add("aboba1");
        stringSet1.add("aboba");
        stringSet1.add("aboba1");
        stringSet1.add("kefteme");
        stringSet1.add("bob");
        System.out.println(stringSet);
        System.out.println(stringSet1);
    }
}


record MapKey(String value) {

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        MapKey mapKey = (MapKey) o;

        return Objects.equals(value, mapKey.value);
    }

    @Override
    public int hashCode() {
        return value != null ? value.hashCode() : 0;
    }

    @Override
    public String toString() {
        return "MapKey{" +
                "value='" + value + '\'' +
                '}';
    }
}

//class MapKeyComparator implements Comparator<MapKey> {
//
//    @Override
//    public int compare(MapKey o1, MapKey o2) {
//        return Integer.compare(o1.value().length(), o2.value().length());
//    }
//}