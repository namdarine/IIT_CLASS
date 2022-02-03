// Fixed Front Queue

package Queue;

public class FixedFrontQueue<T> implements QueueInterface<T> {
	protected final int defCap = 40;
	protected T[] elements;
	protected int num = 0;
	protected int front = 0;
	protected int rear;
	
	// Constructor
	public FixedFrontQueue() {
		elements = (T[]) new Object[defCap];
		rear = defCap - 1;
	}
	
	public FixedFrontQueue (int max) {
		elements = (T[]) new Object[max];
		rear = max - 1;
	}
	
	// Transformers
	public void enqueue (T element) throws QueueOverflowException {
		if (isFull())
			throw new QueueOverflowException ("Enqueue attempted on a full queue");
		// Throws QueueOverflowException if this queue is full.
		
		else {
			rear = (rear + 1) % elements.length;
			elements[rear] = element;
			num = num + 1;
		}
		// Adds new element to the rear of this queue. And adds 1 to 'num' variable.
	}
	
	public T dequeue() throws QueueUnderflowException {
		if (isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on empty queue");
		// Throws QueueUnderflowException if this queue is empty.
		
		else {
			
			T toReturn = elements[front];
			elements[front] = elements[front + 1];
			for (int i = 0; i <= num; i++) {
				elements[i] = elements[i + 1];
			}		// Move elements (which are in this queue. Not array's name) to forward.

			rear = (rear - 1) % elements.length;
			num = num - 1;
			
			return toReturn;
		}
		/* Removes the front element and returns it.
		 * After remove, moves the rest of element to forward, and reduces 1 from 'num' variable.
		 */
	}
	
	// Observers
	public Object front() {
		return front;
	}
	// Returns the front index of this queue.
	
	public Object rear() {
		return rear;
	}
	// Returns the rear index of this queue.
	
	public Object frontEle() {
		return elements[front];
	}
	// Returns the front element of this queue.
	
	public Object rearEle() {
		return elements[rear];
	}
	// Returns the rear element of this queue.
	
	public boolean isEmpty() {
		return num == 0;
	}
	// Returns true if this queue is empty. If not, returns false.
	
	public boolean isFull() {
		return num == elements.length;
	}
	// Returns true if this queue is full. If not, returns false.
	
	public int size() {
		return num;
	}
	// Returns the number of the elements in this queue.
	
	public void dump() throws QueueUnderflowException {
		if (isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on empty queue");
		
		else {
			for (int i = 0; i < num; i++) 
				System.out.print(elements[(i + front) % elements.length] + " ");
			System.out.println();
			
		}
	}
	// Print all elements in this queue

}
