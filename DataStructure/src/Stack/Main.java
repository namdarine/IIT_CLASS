package Stack;

public class Main {

	public static void main(String[] args) throws StackOverflowException, StackUnderflowException {
		ArrayStack<Integer> s = new ArrayStack<>();
		ArrayListStack<Integer> st = new ArrayListStack<>();
		
		s.push(1);
		s.push(2);
		s.push(3);
		s.push(4);
		s.push(5);
		s.push(6);
		s.push(7);
		
		System.out.println(s.top());
		s.pop();
		System.out.println(s.top());
		s.pop();
		System.out.println(s.top());
		
		System.out.println(s.search(2));
		
		st.push(1);
		st.push(2);
		st.push(3);
		st.push(4);
		st.push(5);
		st.push(6);
		st.push(7);
		
		System.out.println(st.top());
		st.pop();
		System.out.println(st.top());
		st.pop();
		System.out.println(st.top());
		System.out.println(st.search(2));

	}

}
