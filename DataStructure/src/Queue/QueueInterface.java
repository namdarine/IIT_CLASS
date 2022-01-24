package Queue;

public interface QueueInterface<T> {
	void enqueue (T element) throws QueueOverflowException;
	/* Adds element to the rear of this queue.
	 * If it is full, throws QueueOverflowException.
	 */
	
	T dequeue() throws QueueUnderflowException;
	/* Removes element from front of this queue and returns it.
	 * if it is empty, throws QueueUnderflowException.
	 */
	
	boolean isFull();
	/* Return true if this queue is full.
	 * If not, return false.
	 */
	
	boolean isEmpty();
	/* Return true if this queue is empty.
	 * if not, return false.
	 */
	
	int size();
	// Returns the number of elements in this queue.
	
	Object front();
	// Returns the front index of this queue.
	
	Object rear();
	// Returns the rear index of this queue.

}
