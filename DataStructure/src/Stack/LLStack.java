// Using Linked List

package Stack;

import java.util.*;

public class LLStack<T> implements StackInterface<T> {
	// Node class
	class Node<T> {
		private T data;
		private Node<T> next;
		
		Node (T data) {
			this.data = data;
			this.next = next;
		}
		
		public void setData(T data) {
			this.data = data;
		}
		
		public T getData() {
			return data;
		}
		
		public void setNext(Node<T> next) {
			this.next = next;
		}
		
		public Node<T> getNext() {
			return next;
		}
	}
	
	protected Node<T> top;
	
	// Constructor
	public LLStack() {
		top = null;
	}
	
	// Transformers
	public void push(T element) {
		Node<T> newNode = new Node<T>(element);
		newNode.setNext(top);
		top = newNode;
	}
	
	public void pop() throws StackUnderflowException {
		if (isEmpty()) 
			throw new StackUnderflowException("Pop attempted on an empty stack.");
		else
			top = top.getNext();
	}
	
	// Observers
	public T top() throws StackUnderflowException {
		if (isEmpty())
			throw new StackUnderflowException("Top attempted on an empty stack.");
		else
			return top.getData();
	}
	
	public boolean isEmpty() {
		return (top == null);
	}
	
	public boolean isFull() {
		return false;
	}	// Because Linked stack is never full



}
