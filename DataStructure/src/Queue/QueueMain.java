package Queue;

public class QueueMain {
	public static void main(String[] args) throws QueueOverflowException, QueueUnderflowException {
		ArrayQueue<Integer> aQue = new ArrayQueue<>();
		FixedFrontQueue<Integer> fQue = new FixedFrontQueue<>();
		
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

	}

}
