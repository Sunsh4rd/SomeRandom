package pet;

public class Pet {
	
	private String name;

	public Pet(String name) {
		this.name = name;
	}

	public String getName() { return this.name; }

	public void speak() {
		System.out.println("I'm pet");
	}
}