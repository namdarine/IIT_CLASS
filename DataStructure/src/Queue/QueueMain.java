package Queue;

public class QueueMain {
	public static void main(String[] args) throws QueueOverflowException, QueueUnderflowException {
		ArrayQueue<Integer> aQue = new ArrayQueue<>();
		FixedFrontQueue<Integer> fQue = new FixedFrontQueue<>();
		
		aQue.enqueue(1);
		aQue.enqueue(2);
		aQue.enqueue(3);
		aQue.enqueue(4);
		aQue.enqueue(5);
		aQue.enqueue(6);
		aQue.enqueue(7);
		aQue.enqueue(8);
		
		System.out.println(aQue.front());
		System.out.println(aQue.rear());
		System.out.println(aQue.size());
		System.out.println(aQue.isEmpty());
		System.out.println(aQue.isFull());
		System.out.println(aQue.dequeue());
		System.out.println(aQue.dequeue());
		System.out.println(aQue.size());
		System.out.println(aQue.front);
		System.out.println(aQue.rear + "\n");
		
		aQue.dump();
		
		fQue.enqueue(1);
		fQue.enqueue(2);
		fQue.enqueue(3);
		fQue.enqueue(4);
		fQue.enqueue(5);
		fQue.enqueue(6);
		fQue.enqueue(7);
		fQue.enqueue(8);
		
		fQue.dump();
		System.out.println(fQue.front());
		System.out.println(fQue.frontEle());
		System.out.println(fQue.rear());
		System.out.println(fQue.size());
		System.out.println(fQue.isEmpty());
		System.out.println(fQue.isFull());
		System.out.println(fQue.dequeue());
		fQue.dump();
		System.out.println(fQue.frontEle());
		System.out.println(fQue.dequeue());
		System.out.println(fQue.size());
		System.out.println("Front index: " + fQue.front());
		System.out.println("Rear index: " +fQue.rear());
		System.out.println(fQue.frontEle());
		fQue.dump();
		System.out.println(fQue.dequeue());
		fQue.dump();
	}

}
