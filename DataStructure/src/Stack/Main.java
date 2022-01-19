package Stack;

public class Main {

	public static void main(String[] args) throws StackOverflowException, StackUnderflowException {
		ArrayStack<Integer> s = new ArrayStack<>();
		
		s.push(1);
		s.push(2);
		s.push(3);
		s.push(4);
		s.push(5);
		s.push(6);
		s.push(7);
		
		s.top();
		s.pop();
		s.top();
		s.pop();
		
		s.search(4);

	}

}
