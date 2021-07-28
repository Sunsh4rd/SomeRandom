package person;

import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonSetter;

import java.util.List;
import java.util.Map;
import java.util.Objects;

public class Person {

    private String _id;
    private int index;
    private String guid;
    private boolean active;
    private String balance;
    private String picture;
    private int age;
    private String eyeColor;
    private String name;
    private String gender;
    private String company;
    private String email;
    private String phone;
    private String address;
    private String about;
    private String registered;
    private int latitude;
    private int longitude;
    private List<String> tags;
    private String greeting;
    private String favoriteFruit;

    public Person() {
    }

    public Person(String _id,
                  int index,
                  String guid,
                  boolean active,
                  String balance,
                  String picture,
                  int age,
                  String eyeColor,
                  String name,
                  String gender,
                  String company,
                  String email,
                  String phone,
                  String address,
                  String about,
                  String registered,
                  int latitude,
                  int longitude,
                  List<String> tags,
                  String greeting,
                  String favoriteFruit) {
        this._id = _id;
        this.index = index;
        this.guid = guid;
        this.active = active;
        this.balance = balance;
        this.picture = picture;
        this.age = age;
        this.eyeColor = eyeColor;
        this.name = name;
        this.gender = gender;
        this.company = company;
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.about = about;
        this.registered = registered;
        this.latitude = latitude;
        this.longitude = longitude;
        this.tags = tags;
        this.greeting = greeting;
        this.favoriteFruit = favoriteFruit;
    }

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }

    @JsonGetter
    public boolean isActive() {
        return active;
    }

    @JsonSetter
    public void setActive(boolean active) {
        this.active = active;
    }

    public String getBalance() {
        return balance;
    }

    public void setBalance(String balance) {
        this.balance = balance;
    }

    public String getPicture() {
        return picture;
    }

    public void setPicture(String picture) {
        this.picture = picture;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getEyeColor() {
        return eyeColor;
    }

    public void setEyeColor(String eyeColor) {
        this.eyeColor = eyeColor;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }

    public String getRegistered() {
        return registered;
    }

    public void setRegistered(String registered) {
        this.registered = registered;
    }

    public int getLatitude() {
        return latitude;
    }

    public void setLatitude(int latitude) {
        this.latitude = latitude;
    }

    public int getLongitude() {
        return longitude;
    }

    public void setLongitude(int longitude) {
        this.longitude = longitude;
    }

    public List<String> getTags() {
        return tags;
    }

    public void setTags(List<String> tags) {
        this.tags = tags;
    }

    public String getGreeting() {
        return greeting;
    }

    public void setGreeting(String greeting) {
        this.greeting = greeting;
    }

    public String getFavoriteFruit() {
        return favoriteFruit;
    }

    public void setFavoriteFruit(String favoriteFruit) {
        this.favoriteFruit = favoriteFruit;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return _id == person._id
             && index == person.index
             && active == person.active
             && age == person.age
             && latitude == person.latitude
             && longitude == person.longitude
             && Objects.equals(guid, person.guid)
             && Objects.equals(balance, person.balance)
             && Objects.equals(picture, person.picture)
             && Objects.equals(eyeColor, person.eyeColor)
             && Objects.equals(name, person.name)
             && Objects.equals(gender, person.gender)
             && Objects.equals(company, person.company)
             && Objects.equals(email, person.email)
             && Objects.equals(phone, person.phone)
             && Objects.equals(address, person.address)
             && Objects.equals(about, person.about)
             && Objects.equals(registered, person.registered)
             && Objects.equals(tags, person.tags)
             && Objects.equals(greeting, person.greeting)
             && Objects.equals(favoriteFruit, person.favoriteFruit);
    }

    @Override
    public int hashCode() {
        return Objects.hash(_id,
                index,
                guid,
                active,
                balance,
                picture,
                age,
                eyeColor,
                name,
                gender,
                company,
                email,
                phone,
                address,
                about,
                registered,
                latitude,
                longitude,
                tags,
                greeting,
                favoriteFruit);
    }

    @Override
    public String toString() {
        return "Person{" +
                "_id=" + _id +
                ", index=" + index +
                ", guid='" + guid + '\'' +
                ", isActive=" + active +
                ", balance='" + balance + '\'' +
                ", picture='" + picture + '\'' +
                ", age=" + age +
                ", eyeColor='" + eyeColor + '\'' +
                ", name='" + name + '\'' +
                ", gender='" + gender + '\'' +
                ", company='" + company + '\'' +
                ", email='" + email + '\'' +
                ", phone='" + phone + '\'' +
                ", address='" + address + '\'' +
                ", about='" + about + '\'' +
                ", registered='" + registered + '\'' +
                ", latitude=" + latitude +
                ", longitude=" + longitude +
                ", tags=" + tags +
                ", greeting='" + greeting + '\'' +
                ", favoriteFruit='" + favoriteFruit + '\'' +
                '}';
    }
}
