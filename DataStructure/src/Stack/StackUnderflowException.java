package Stack;

@SuppressWarnings("serial")
public class StackUnderflowException extends Exception {
	public StackUnderflowException() {
		super();
	}
	
	public StackUnderflowException (String message) {
		super(message);
	}

}
