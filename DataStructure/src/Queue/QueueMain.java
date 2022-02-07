package Queue;

public class QueueMain {
	public static void main(String[] args) throws QueueOverflowException, QueueUnderflowException {
		ArrayQueue<Integer> aQue = new ArrayQueue<>();
		FixedFrontQueue<Integer> fQue = new FixedFrontQueue<>();
		LLQueue<Integer> lQue = new LLQueue<>();
		CLQueue<Integer> cQue = new CLQueue<>();
		
		System.out.println("Floating front Queue: ");
		aQue.enqueue(1);
		aQue.enqueue(2);
		aQue.enqueue(3);
		aQue.enqueue(4);
		aQue.enqueue(5);
		aQue.enqueue(6);
		aQue.enqueue(7);
		aQue.enqueue(8);
		
		System.out.println("Front element is: " + aQue.front());
		System.out.println("Rear element is: " + aQue.rear());
		System.out.println("Queue's size is: " + aQue.size());
		System.out.println("Is Queue empty? " + aQue.isEmpty());
		System.out.println("Is Queue full? " + aQue.isFull());
		System.out.println(aQue.dequeue());
		System.out.println(aQue.dequeue());
		System.out.println("Queue's size is after dequeue twice: " + aQue.size());
		System.out.println("After dequeue twice, front element is: " + aQue.front);
		System.out.println("After dequeue twice, rear element is: " + aQue.rear);
		aQue.dump();
		
		System.out.println("\nFixed front Queue: ");
		fQue.enqueue(11);
		fQue.enqueue(12);
		fQue.enqueue(13);
		fQue.enqueue(14);
		fQue.enqueue(15);
		fQue.enqueue(16);
		fQue.enqueue(17);
		fQue.enqueue(18);
		
		fQue.dump();
		System.out.println("Front index is: " + fQue.front());
		System.out.println("Front element is: " + fQue.frontEle());
		System.out.println("Rear index is: " + fQue.rear());
		System.out.println("Rear element is: " + fQue.rearEle());
		System.out.println("Queue's size is: " + fQue.size());
		System.out.println("Is Queue empty? " + fQue.isEmpty());
		System.out.println("Is Queue full? " + fQue.isFull());
		System.out.println(fQue.dequeue());
		System.out.println(fQue.dequeue());
		System.out.println("Queue's size is after dequeue twice: " + fQue.size());
		System.out.println("After dequeue twice, front index is: " + fQue.front());
		System.out.println("After dequeue twice, front element is: " + fQue.frontEle());
		System.out.println("After dequeue twice, rear index is: " + fQue.rear());
		System.out.println("After dequeue twice, rear element is: " + fQue.rearEle());
		fQue.dump();
		
		System.out.println("\nLinked-list Queue: ");
		lQue.enqueue(11);
		lQue.enqueue(12);
		lQue.enqueue(13);
		lQue.enqueue(14);
		lQue.enqueue(15);
		lQue.enqueue(16);
		lQue.enqueue(17);
		lQue.enqueue(18);
		
		lQue.dump();
		System.out.println("\nFront index is: " + lQue.front());
		System.out.println("Rear index is: " + lQue.rear());
		System.out.println("Queue's size is: " + lQue.size());
		System.out.println("Is Queue empty? " + lQue.isEmpty());
		System.out.println("Is Queue full? " + lQue.isFull());
		System.out.println(lQue.dequeue());
		System.out.println(lQue.dequeue());
		System.out.println("Queue's size is after dequeue twice: " + lQue.size());
		System.out.println("After dequeue twice, front element is: " + lQue.front());
		System.out.println("After dequeue twice, rear element is: " + lQue.rear());
		lQue.dump();
		lQue.dequeue();
		lQue.dequeue();
		lQue.dequeue();
		lQue.dequeue();

		System.out.println("\nCircular Linked-list Queue: ");
		cQue.enqueue(11);
		cQue.enqueue(12);
		cQue.enqueue(13);
		cQue.enqueue(14);
		cQue.enqueue(15);
		cQue.enqueue(16);
		cQue.enqueue(17);
		cQue.enqueue(18);
		
		cQue.dump();
		System.out.println("\nFront index is: " + cQue.front());
		System.out.println("Rear index is: " + cQue.rear());
		System.out.println("Queue's size is: " + cQue.size());
		System.out.println("Is Queue empty? " + cQue.isEmpty());
		System.out.println("Is Queue full? " + cQue.isFull());
		System.out.println(cQue.dequeue());
		System.out.println(cQue.dequeue());
		System.out.println("Queue's size is after dequeue twice: " + cQue.size());
		System.out.println("After dequeue twice, front element is: " + cQue.front());
		System.out.println("After dequeue twice, rear element is: " + cQue.rear());
		cQue.dump();
		System.out.println("\n" + cQue.dequeue());
		System.out.println(cQue.dequeue());
		System.out.println(cQue.dequeue());
		System.out.println(cQue.dequeue());
		System.out.println("After dequeue four times, front element is: " + cQue.front());
		System.out.println("After dequeue four times, rear element is: " + cQue.rear());
		cQue.dump();
		cQue.enqueue(21);
		cQue.enqueue(23);
		cQue.enqueue(24);
		System.out.println("\nAfter enqueue, front element is: " + cQue.front());
		System.out.println("After enqueue, rear element is: " + cQue.rear());
		cQue.dump();


	}

}
