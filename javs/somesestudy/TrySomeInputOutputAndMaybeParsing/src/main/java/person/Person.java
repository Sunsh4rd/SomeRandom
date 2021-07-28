package person;

import java.util.List;
import java.util.Objects;

public class Person {
    private int id;
    private String guid;
    private String name;
    private List<String> tags;

    public Person() {
    }

    public Person(int id, String guid, String name, List<String> tags) {
        this.id = id;
        this.guid = guid;
        this.name = name;
        this.tags = tags;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setTags(List<String> tags) {
        this.tags = tags;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return id == person.id
                && Objects.equals(guid, person.guid)
                && Objects.equals(name, person.name)
                && Objects.equals(tags, person.tags);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, guid, name, tags);
    }

    @Override
    public String toString() {
        return "Person{" +
                "id=" + id +
                ", guid='" + guid + '\'' +
                ", name='" + name + '\'' +
                ", tags=" + tags +
                '}';
    }
}
