package Stack;

public interface StackInterface<T> {
	void push (T element) throws StackOverflowException;	// If the stack is full, throws StackOverflowException.
	// Because if the stack is full, there is no room for new element to add onto this stack.
	// Otherwise add element at the top of this stack.
	
	void pop() throws StackUnderflowException;	// If the stack is empty, throws StackUnderflowException.
	// Because if the stack is empty, there is nothing to remove from this stack.
	// Otherwise remove top element from this stack.
	
	T top() throws StackUnderflowException;    // If the stack is empty, throws StackUnderflowException.
	// Because there are not any elements in this stack even the top of this stack.
	// Otherwise returns top element of this stack.
	
	boolean isEmpty();
	// If the stack is empty, returns true. Otherwise false.
	
	boolean isFull();
	// If the stack is full, returns true. Otherwise false.
	
	int search(T value);
	// Returns the position where a value is on this stack. Returns '-1' if the value does not on the stack.

}
