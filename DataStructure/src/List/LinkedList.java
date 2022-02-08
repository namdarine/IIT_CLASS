package List;

import java.util.*;

public class LinkedList<T> implements ListInterface<T> {
	class Node<T> {
		private T data;
		private Node<T> next;
		
		Node (T data) {
			this.data = data;
			this.next = next;
		}
	}
	
	private Node<T> head;
	private Node<T> tail;
	private int size;
	
	// Constructor
	public LinkedList() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}
	
	// Transformer
	public boolean add (T value) {
		addEnd(value);
		return true;
	}
	
	// Add in the front
	public void addFront (T value) {
		Node<T> newNode = new Node<T>(value);
		newNode.next = head;
		head = newNode;
		size++;
		
		if(head.next == null) tail = head;
	}
	
	// Add in the end
	public void addEnd (T value) {
		Node<T> newNode = new Node<T>(value);
		if(size == 0) {
			addFront(value);
			return;
		}
		
		tail.next = newNode;
		tail = newNode;
		size++;
	}
	
	public void add (int index, T value) {				// Add new value in specific index
		if (index > size || index < 0) throw new IndexOutOfBoundsException();
		
		if (index == 0) {
			addFront(value);
			return;
		}
		
		if (index == size) {
			addEnd(value);
			return;
		}
		
		Node<T> pre_Node = search(index - 1);
		Node<T> next_Node = pre_Node.next;
		Node<T> newNode = new Node<T>(value);
		
		pre_Node.next = null;
		pre_Node.next = newNode;
		newNode.next = next_Node;
		size++;
	}
	
	public T remove() {							// Remove front node
		Node<T> headNode = head;
		if (headNode == null) throw new NoSuchElementException();
		
		T element = headNode.data;
		Node<T> nextNode = head.next;
		head.data = null;
		head.next = null;
		head = nextNode;
		size--;
		
		if (size == 0) tail = null;
		
		return element;
	}
	
	public T remove (int index) {				// Remove specific index
		if (index == 0) return remove();
		
		if (index >= size || size <0) throw new IndexOutOfBoundsException();
		
		Node<T> preNode = search(index - 1);
		Node<T> removedNode = preNode.next;
		Node<T> nextNode = removedNode.next;
		
		T element = removedNode.data;
		preNode.next = nextNode;
		removedNode.next = null;
		removedNode.data = null;
		size--;
		
		return element;
	}
	
	public boolean remove (Object value) {		// Remove specific value
		Node<T> preNode = head;
		boolean hasValue = false;
		Node<T> ptr = head;
		
		for (; ptr != null; ptr = ptr.next) {
			if (value.equals(ptr.data)) {
				hasValue = true;
				break;
			}
			
			preNode = ptr;
		}
		
		if (ptr == null) return false;
		if (ptr.equals(head)) {
			remove();
			return true;
		}
		
		else {
			preNode.next = ptr.next;
			ptr.data = null;
			ptr.next = null;
			size--;
			return true;
		}
	}
	
	public void set (int index, T value) {			// Replace value in specific index
		Node<T> replaceNode = search(index);
		replaceNode.data = null;
		replaceNode.data = value;
	}
	
	public void clear() {							// Clear this list
		for (Node<T> ptr = head; ptr != null;) {
			Node<T> nextNode = ptr.next;
			ptr.data = null;
			ptr.next = null;
			ptr = nextNode;
		}
		
		head = tail = null;
		size = 0;
	}
	
	public boolean contains (Object value) {		// Check the value is in this list.
		return indexOf(value) >= 0;
	}
	
	public int indexOf (Object value) {				// Get the index of value in this list.
		int index = 0;
		for (Node<T> ptr = head; ptr != null; ptr = ptr.next) {
			if (value.equals(ptr.data)) return index;
			index++;
		}
		
		return -1;
	}
	
	public T get (int index) {			// Get the value of the index in this list.
		return search(index).data;
	}
	
	private Node<T> search(int index) {
		if (index < 0 || index >= size) throw new IndexOutOfBoundsException();
		
		Node<T> ptr = head;
		for (int i = 0; i < index; i++) 
			ptr = ptr.next;
		return ptr;
	}
	
	public int size() {
		return size;
	}
	
	public void dump() {
		Node<T> ptr = head;
		while (ptr != null) {
			System.out.println(ptr.data);
			ptr = ptr.next;
		}
	}
	
	public void sort() {
		sort(null);
	}
	
	@SuppressWarnings({"unchecked", "rawtypes"})
	public void sort(Comparator<? super T> c) {
		Object[] a = this.toArray();
		Arrays.sort(a, (Comparator) c);
		
		int i = 0;
		for (Node<T> ptr = head; ptr != null; ptr = ptr.next, i++)
			ptr.data = (T) a[i];
	}
	
	// Convert linked list to array
	@SuppressWarnings("unchecked")
	public <E> E[] toArray(E[] a) {
		if (a.length < size)
			a = (E[]) java.lang.reflect.Array.newInstance(a.getClass().getComponentType(),size);
		
		int i = 0;
		Object[] result = a;
		for (Node<T> ptr = head; ptr != null; ptr = ptr.next)
			result[i++] = ptr.data;
		
		return a;	
	}
	
	public Object[] toArray() {
		Object[] array = new Object[size];
		int idx = 0;
		for (Node<T> ptr = head; ptr != null; ptr = ptr.next)
			array[idx++] = (T) ptr.data;
		
		return array;
	}

}
