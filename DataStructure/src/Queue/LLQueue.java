// Using Linked list Queue
package Queue;

public class LLQueue<T> implements QueueInterface<T> {
	// Node class
	class Node<T> {
		private T data;
		private Node<T> next;
		
		Node(T data) {
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
	
	protected Node<T> front;
	protected Node<T> rear;
	protected int num = 0;
	
	// Constructor
	public LLQueue() {
		this.front = null;
		this.rear = null;
	}
	
	// Transformer
	public void enqueue(T element) {
		Node<T> newNode = new Node<T>(element);
		if (isEmpty() == true) {			// If this queue is empty, add new element in the front of this queue.
			newNode.next = front;			// Make new node.
			front = newNode;				// Set new front.
			
			if (front.next == null)
				rear = front;
		}
		
		else 								// If this queue is not empty, add new element in the rear of this queue.
			rear.next = newNode;			// Make new node and linked it.
		
		rear = newNode;						// Set new rear.
		num++;
	}
	
	public T dequeue() throws QueueUnderflowException {
		if (isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on empty queue.");
		
		else {
			T element;
			element = front.getData();
			front = front.getNext();
			
			if (front == null)
				rear = null;
			
			num--;
			return element;
		}
	}
	
	public Object front() {
		return front.getData();
	}
	
	public Object rear() {
		return rear.getData();
	}
	
	public boolean isEmpty() {
		return (num == 0);
	}
	
	public boolean isFull() {
		return false;
	}
	
	public int size() {
		return num;
	}
	
	public void dump() {			// List all elements in this queue.
		Node<T> ptr = front;
		while (ptr != null) {
			System.out.println(ptr.data);
			ptr = ptr.next;
		}
	}

}
