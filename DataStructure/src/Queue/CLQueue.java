// Using Circular linked Queue
package Queue;

public class CLQueue<T> implements QueueInterface<T> {
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
	
	protected Node<T> front;
	protected Node<T> rear;
	protected int num = 0;
	
	// Constructor
	public CLQueue() {
		this.front = null;
		this.rear = null;
	}
	
	// Transformer
	public void enqueue(T element) {
		Node<T> newNode = new Node<T>(element);
		if (isEmpty()) {
			newNode.next = front;
			front = newNode;
			
			if (front.next == null)
				rear = front;
		}
		
		else
			rear.next = newNode;
		
		rear = newNode;
		rear.next = front;					// Connect rear and front to make it circle.
		num++;
	}
	
	public T dequeue() throws QueueUnderflowException {
		if(isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on empty queue.");
		
		else {
			T element;
			if (front == rear) {
				element = front.getData();
				front = null;
				rear = null;				
			}
			
			else {
				Node<T> newNode = front;
				element = newNode.data;
				front = front.next;
				rear.next = front;			// Connect rear and front to make it circle.
			}
			
			num--;
			return element;
		}
	}
	
	// Observers
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
		while (ptr.next != front) {
			System.out.printf("%d ", ptr.data);
			ptr = ptr.next;
		}
		System.out.printf("%d ", ptr.data);
	}

}
