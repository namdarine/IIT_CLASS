package BST;

public class BSTNode<T> {
	private T key;
	private T data;
	private BSTNode<T> left;
	private BSTNode<T> right;
	
	// Constructor
	public BSTNode(T key) {
		this.key = key;
		this.data = data;
		left = null;
		right = null;
	}
	
	// Setter
	public void setKey (T key) {
		this.key = key;
	}
	
	public void setData (T data) {
		this.data = data;
	}
	
	public void setLeft (BSTNode<T> link) {
		left = link;
	}
	
	public void setRight (BSTNode<T> link) {
		right = link;
	}
	
	// Getter
	public T getKey() {
		return key;
	}
	
	public T getData() {
		return data;
	}
	
	public BSTNode<T> getLeft() {
		return left;
	}
	
	public BSTNode<T> getRight() {
		return right;
	}
	
	void print() {
		System.out.println(data);
	}

}
