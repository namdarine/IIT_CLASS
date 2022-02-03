/* Using Array Bounded List
 * Known as "Floating Front Queue"
 */

package Queue;

public class ArrayQueue<T> implements QueueInterface<T> {
	protected final int defCap = 50;	// Set the size of this Queue's capacity
	protected T[] elements;    			// Holds queue elements
	protected int num = 0;				// Number of elements in this queue
	protected int front = 0;			// Index of front of this queue
	protected int rear;					// Index of rear of this queue
	
	// Constructor
	public ArrayQueue () {
		elements = (T[]) new Object[defCap];
		rear = defCap - 1;
	}
	
	public ArrayQueue(int max) {
		elements = (T[]) new Object[max];
		rear = max - 1;
	}
	
	// Transformers
	@Override
	public void enqueue(T element) throws QueueOverflowException {
		if (isFull())
			throw new QueueOverflowException("Enqueue attempted on a full queue.");
		// Throws QueueOverflowException if this queue is full
		
		else {
			rear = (rear + 1) % elements.length;
			elements[rear] = element;
			num = num + 1;
			
			// Adds element to the rear of this queue and adds 1 to 'num' variable.
		}
	}
	
	@Override
	public T dequeue() throws QueueUnderflowException {
		if (isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on a empty queue.");
		// Throws QueueUnderflowException if this queue is empty.
		
		else {
			T toReturn = elements[front];
			elements[front] = null;
			front = (front + 1) % elements.length;
			num = num - 1;
			return toReturn;
			
			/* Removes front element of this queue and returns it.
			 * And removes 1 from 'num' variable.
			 */
		}
	}
	
	// Observers
	@Override
	public boolean isFull() {
		return num == elements.length;
		// Returns true if this queue is full. If not, returns false.
	}
	
	@Override
	public boolean isEmpty() {
		return num == 0;
		// Returns true if this queue is empty. If not, returns false.
	}
	
	@Override
	public int size() {
		return num;
		// Returns the number of the elements in this queue.
	}
	
	public Object front() {
		return elements[front];
	}
	// Returns the front element of this queue
	
	public Object rear() {
		return elements[rear];
	}
	// Returns the rear element of this queue
	
	public void dump() throws QueueUnderflowException {
		if (isEmpty())
			throw new QueueUnderflowException("Dequeue attempted on empty queue");
		
		else {
			for (int i = 0; i < num; i++) 
				System.out.print(elements[(i + front) % elements.length] + " ");
			System.out.println();
			
		}
	}

}
