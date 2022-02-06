package Stack;

public class Main {

	public static void main(String[] args) throws StackOverflowException, StackUnderflowException {
		ArrayStack<Integer> s = new ArrayStack<>();
		ArrayListStack<Integer> st = new ArrayListStack<>();
		LLStack<Integer> ls = new LLStack<>();
		
		System.out.println("Array Bounded List Stack:\n");
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
		
		System.out.println("Array Unbounded List Stack:\n");
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
		
		System.out.println("Linked List Stack:\n");
		ls.push(1);
		ls.push(2);
		ls.push(3);
		ls.push(4);
		ls.push(5);
		ls.push(6);
		ls.push(7);
		
		System.out.println(ls.top());
		ls.pop();
		System.out.println(ls.top());
		ls.pop();
		System.out.println(ls.top());

	}

}
