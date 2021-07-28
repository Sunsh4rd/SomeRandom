package test;

public class Test {
	
	public static void main(String[] args) {
		CounterC cc = new CounterC(4);
		cc.add(5);
		cc.minus(5);
	}
}

abstract class Counter {

	int c;

	Counter(int c) {
		this.c = c;
	}

	abstract void add(int x);

	abstract void minus(int x);
}

class CounterC extends Counter {

	CounterC(int c) {
		super(c);
	}

	void add(int x) {
		System.out.println(this.c + x);
	}

	void minus(int x) {
		System.out.println(this.c - x);
	}
}