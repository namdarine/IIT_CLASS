// Using Array Unbounded List
package Stack;

import java.util.*;

public class ArrayListStack<T> implements StackInterface<T> {
	protected ArrayList<T> elements;	// Store stack elements in array list

	
	public ArrayListStack() {
		elements = new ArrayList<T>();
	}
	
	public void push(T element) {
		elements.add(element);
	}
	
	public void pop() throws StackUnderflowException {
		if (isEmpty())
			throw new StackUnderflowException();
		
		else
			elements.remove(elements.size() - 1);
	}
	
	@Override
	public T top() throws StackUnderflowException {
		T topStack = null;
	
		if(isEmpty())
			throw new StackUnderflowException();
		
		else
			topStack = elements.get(elements.size() - 1);
		
		return topStack;
	}
	
	public boolean isEmpty() {
		return (elements.size() == 0);
	}

	@Override
	public boolean isFull() {

		return false;
		// Because Array list does not full. There is not default capacity of stack.
	}

	@Override
	public int search(T value) {
		for (int index = elements.size() -1; index >= 0; index--) {
			if (elements.contains(value))
				return (elements.size() - index);
				
			// If found the value, returns the position of the value in this stack.
		}
			
		return -1;
		// If not, returns -1.
	}


}
