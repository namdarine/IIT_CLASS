// Using Array Bounded List Stack
package Stack;

public class ArrayStack<T> implements StackInterface<T> {
	protected final int DefCap = 50;	// Set 50 as default capacity
	protected T[] elements;    // Storage of stack elements
	protected int topIndex = -1;    // Index of top element in this stack. If this stack is empty, 'topIndex' is -1
	
	// Constructor
	@SuppressWarnings("unchecked")
	public ArrayStack() {
		elements = (T[]) new Object[DefCap];
	}
	
	@SuppressWarnings("unchecked")
	public ArrayStack(int max) {
		elements = (T[]) new Object[max];
	}
	
	// Transformers
	public void push(T element) throws StackOverflowException {
		if (isFull())
			throw new StackOverflowException("Push attempted on a full stack.");
		// Throw StackOverflowException if this stack is full.
		
		else {
			topIndex++;
			elements[topIndex] = element;
		}
		// If not, add element at the top of this stack.
	}
	
	public void pop() throws StackUnderflowException {
		if (isEmpty())
			throw new StackUnderflowException("Pop attempted on empty stack.");
		// Throw StackUnderflowException if this stack is empty.
		
		else {
			elements[topIndex] = null;
			topIndex--;
		}
	}
	
	// Observers
	public T top() throws StackUnderflowException {
		T topStack = null;
		
		if (isEmpty())
			throw new StackUnderflowException("Top attempted on empty stack.");
		// Throw StackUnderflowException if this stack is empty.
		
		else 
			topStack = elements[topIndex];
		
		return topStack;
		// Return top element of this stack.
	}
	
	public boolean isEmpty() {
		return (topIndex == -1);
		// Return true if this stack is empty. 
	}
	
	public boolean isFull() {
		return (topIndex == elements.length -1);
		// Return true if this stack is full.
	}
	
	public int search(T value) {
		for (int index = topIndex -1; index >= 0; index--) {
			if (elements[index].equals(value))
				return topIndex - index;
			
			// If found the value, returns the position of the value in this stack.
		}
		
		return -1;
		// If not, returns -1.
	}

}
