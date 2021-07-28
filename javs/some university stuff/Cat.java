package cat;

import pet.Pet;

public class Cat extends Pet {

	public Cat(String name) {
		super(name);
	}

	public void speak() {
		System.out.printf("Meow, I'm %s\n", getName());
	}
}