package List;

import java.util.*;

public class DoubleLinkedList<T> implements ListInterface<T> {
	// Node class
	class Node<T> {
		private T data;
		private Node<T> next;
		private Node<T> prev;
		
		Node (T data) {
			this.data = data;
			this.next = next;
			this.prev = prev;
		}
	}
	
	private Node<T> head;
	private Node<T> tail;
	private int size;
	
	// Constructor
	public DoubleLinkedList() {
		this.head = null;
		this.tail = null;
		this.size = 0;
	}
	
	// Transformer
	public boolean add (T value) {
		addEnd(value);
		return true;
	}
	
	public void add (int index, T value) {
		if (index > size || index < 0) throw new IndexOutOfBoundsException();
		
		if (index == 0) {
			addFront(value);
			return;
		}
		
		if (index == size) {
			addEnd(value);
			return;
		}
		
		Node<T> pre_node = search(index - 1);
		Node<T> next_node = pre_node.next;
		Node<T> newNode = new Node<T>(value);
		
		// Disconnect the link
		pre_node.next = null;
		next_node.prev = null;
		
		pre_node.next = newNode;
		
		// Connect the link
		newNode.prev = pre_node;
		newNode.next = next_node;
		next_node.prev = newNode;
		size++;
	}
	
	public void addFront (T value) {
		Node<T> newNode = new Node<T>(value);
		newNode.next = head;
		
		if (head != null) head.prev = newNode;
		
		head = newNode;
		size++;
		
		if (head.next == null) tail = head;
	}
	
	public void addEnd(T value) {
		Node<T> newNode = new Node<T>(value);
		
		if (size == 0) {
			addFront(value);
			return;
		}
		
		tail.next = newNode;
		newNode.prev = tail;
		tail = newNode;
		size++;
	}
	
	public T remove() {
		Node<T> headNode = head;
		if (headNode == null) throw new NoSuchElementException();
		
		T element = headNode.data;
		Node<T> nextNode = head.next;
		head.data = null;
		head.next = null;
		if (nextNode != null)
			nextNode.prev = null;
		
		head = nextNode;
		size--;
		
		if (size == 0)
			tail = null;
		return element;
	}
	
	public T remove (int index) {
		if (index >= size || index < 0)
			throw new IndexOutOfBoundsException();
		
		if (index == 0) {
			T element = head.data;
			remove();
			return element;
		}
		
		Node<T> preNode = search(index - 1);
		Node<T> removedNode = preNode.next;
		Node<T> nextNode = removedNode.next;
		T element = removedNode.data;
		
		preNode.next = null;
		removedNode.next = null;
		removedNode.prev = null;
		removedNode.data = null;
		
		if (nextNode != null) {
			nextNode.prev = null;
			nextNode.prev = preNode;
			preNode.next = nextNode;
		}
		
		else
			tail = preNode;
		
		size--;
		return element;
	}
	
	public boolean remove (Object value) {
		Node<T> preNode = head;
		Node<T> ptr = head;
		
		for (; ptr != null; ptr = ptr.next) {
			if (value.equals(ptr.data))
				break;
			preNode = ptr;
		}
		
		if (ptr == null)
			return false;
		
		if (ptr.equals(head)) {
			remove();
			return true;
		}
		
		else {
			Node<T> nextNode = ptr.next;
			preNode.next = null;
			ptr.data = null;
			ptr.next = null;
			ptr.prev = null;
			
			if (nextNode != null) {
				nextNode.prev = null;
				nextNode.prev = preNode;
				preNode.next = nextNode;
			}
			
			else
				tail = preNode;
			
			size--;
			return true;
		}
	}
	
	public int indexOf (Object o) {
		int index = 0;
		
		for (Node<T> ptr = head; ptr != null; ptr = ptr.next) {
			if (o.equals(ptr.data))
				return index;
		}
		
		return -1;
	}
	
	public boolean contains (Object value) {
		return indexOf(value) >= 0;
	}
	
	private Node<T> search (int index) {
		if (index < 0 || index >= size)
			throw new IndexOutOfBoundsException();
		
		if (index > size / 2) {
			Node<T> ptr = tail;
			for (int i = size - 1; i > index; i--)
				ptr = ptr.prev;
			
			return ptr;
		}
		
		else {
			Node<T> ptr = head;
			for (int i = 0; i < index; i++)
				ptr = ptr.next;
			return ptr;
		}
	}
	
	public void dump() {
		Node<T> ptr = head;
		while (ptr != null) {
			System.out.println(ptr.data);
			ptr = ptr.next;
		}
	}

	public void set(int index, T value) {			// Replace value in specific index
		Node<T> replaceNode = search(index);
		replaceNode.data = null;
		replaceNode.data = value;
		
	}

	public void clear() {							// Clear this list
		for (Node<T> ptr = head; ptr != null;) {
			Node<T> nextNode = ptr.next;
			ptr.data = null;
			ptr.prev = null;
			ptr.next = null;
			ptr = nextNode;
		}
		
	}

	public T get(int index) {						// Get the value of the index in this list
		return search(index).data;
	}

	public int size() {
		return size;
	}

	public void sort() {
		sort(null);
		
	}
	
	@SuppressWarnings({"unchecked", "rawtypes"})
	public void sort(Comparator<? super T> c) {
		Object[] a = this.toArray();
		Arrays.sort(a, (Comparator) c);
		
		int i = 0;
		for (Node<T> ptr = head; ptr!= null; ptr = ptr.next, i++)
			ptr.data = (T) a[i];
	}
	
	// Convert linked list to array
	@SuppressWarnings("unchecked")
	public <E> E[] toArray(E[] a) {
		if (a.length < size)
			a = (E[]) java.lang.reflect.Array.newInstance(a.getClass().getComponentType(), size);
		
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
