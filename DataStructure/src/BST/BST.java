package BST;

import java.util.*;
import Stack.*;

public class BST<T> {
	private BSTNode<T> root;
	private Comparator<? super T> comparator = null;
	
	protected boolean found;
	
	// Constructor
	public BST() {
		root = null;
	}
	
	public BST(Comparator<? super T> c) {
		this();
		comparator = c;
	}
	
	// Transformers
	// Add Node T to subtree
	private void addNode (BSTNode<T> node, T key) {
		int cond = compa(key, node.getKey());
		if (cond == 0)							// Means that two keys are same.
			return;
		
		else if (cond < 0) {					// New node's key is smaller than root node.
			if (node.getLeft() == null)
				node.setLeft(new BSTNode<T>(key));
			else
				addNode(node.getLeft(), key);
		}
		
		else {									// New node's key is bigger than root node.
			if (node.getRight() == null)
				node.setRight(new BSTNode<T>(key));
			
			else
				addNode(node.getRight(), key);
		}
	}
	
	// Add Node
	public void add(T key) {
		if (root == null)						// Add key to the root.
			root = new BSTNode<T>(key);
		else
			addNode(root, key);
	}
	
	// Remove node
	public boolean remove (T target) {
		root = remove(target, root);
		return found;
	}
	
	private BSTNode<T> remove (T target, BSTNode<T> node) {
		if (node == null)
			found = false;
		
		else if (compa(target, node.getKey()) < 0)
			node.setLeft(remove(target, node.getLeft()));
		
		else if (compa(target, node.getKey()) > 0)
			node.setRight((remove(target, node.getRight())));
			
		else {
			node = removeNode(node);
			found = true;
		}
			
		return node;	
	}
	
	private BSTNode<T> removeNode (BSTNode<T> node) {
		T data;
		if (node.getLeft() == null)
			return node.getRight();
		
		else if (node.getRight() == null)
			return node.getLeft();
		
		else {
			data = getPredecessor(node.getLeft());
			node.setKey(data);
			node.setLeft(remove(data, node.getLeft()));
			return node;
		}
	}
	
	private T getPredecessor (BSTNode<T> subtree) {
		BSTNode<T> temp = subtree;
		while (temp.getRight() != null)
			temp = temp.getRight();
		
		return temp.getKey();
	}
	
	// Compare two keys
	@SuppressWarnings("unchecked")
	private int compa(T key1, T key2) {
		return (comparator == null) ? ((Comparable<T>) key1).compareTo(key2)
				: comparator.compare(key1,  key2);
	}
	
	// Search with 'key'
	public T search(T key) {
		BSTNode<T> ptr = root;
		while (true) {
			if (ptr == null)
				return null;
			
			// Compare key and key of pointer
			int cond = compa(key, ptr.getKey());
			if (cond == 0)
				return ptr.getData();
			
			// If key is smaller, then search in left subtree
			else if (cond < 0)
				ptr = ptr.getLeft();
			
			// If key is bigger, search in right subtree
			else
				ptr = ptr.getRight();
		}
	}
	
	// Returns true if BST contains a node. Otherwise, returns false.
	public boolean contain (T target) {
		return contain(target, root);
	}
	
	public boolean contain (T target, BSTNode<T> node) {
		if (node == null)							// Target is not found.
			return false;
		
		else if (compa(target, node.getKey()) < 0)	// Search left subtree.
			return contain(target, node.getLeft());
		
		else if (compa(target, node.getKey()) > 0)	// Search Right subtree.
			return contain(target, node.getRight());
		
		else										// Target is found.
			return true;
	}
	
	// Returns information from node of BST if it's exist. Otherwise, returns null.
	public T get (T target) {
		return get(target, root);
	}
	
	private T get (T target, BSTNode<T> node) {
		if (node == null)							// Target is not found.
			return null;
		
		else if (compa(target, node.getKey()) < 0)	// Get from left subtree.
			return get(target, node.getLeft());
		
		else if (compa(target, node.getKey()) > 0)	// Get from right subtree.
			return get (target, node.getRight());
		
		else										// Target is found.
			return node.getKey();
	}
	
	// Observers
	// Calculate size of the tree with recursive method
	public int recSize() {
		return recSize(root);
	}
	
	public int recSize(BSTNode<T> node) {
		if (node == null)
			return 0;
		
		else
			return 1 + recSize(node.getLeft()) + recSize(node.getRight());
	}
	
	// Calculate size of the tree with iterative method
	public int iterSize() throws StackOverflowException, StackUnderflowException {
		int count = 0;
		if (root != null) {
			ArrayStack<BSTNode<T>> nodeStack = new ArrayStack<BSTNode<T>>();
			BSTNode<T> currNode;
			nodeStack.push(root);
			while (!nodeStack.isEmpty()) {
				currNode = nodeStack.top();
				nodeStack.pop();
				count++;
				
				if(currNode.getLeft() != null)
					nodeStack.push(currNode.getLeft());
				
				if (currNode.getRight() != null)
					nodeStack.push(currNode.getRight());
			}
		}
		
		return count;
	}
	
	// Find maximum depth of the tree
	public int maxDepth() {
		return findDepth(root, 0);
	}
	
	public int findDepth(BSTNode<T> node, int depth) {
		if (node == null)
			return depth;
		
		return Math.max(findDepth(node.getLeft(), depth + 1),  findDepth(node.getRight(), depth + 1));
	}
	
	// Print traversal of tree with three different methods
	public void inorder() {
		inorder(root);
	}
	
	private void inorder(BSTNode<T> node) {
		if (node != null) {
			inorder(node.getLeft());				// Left subtree
			System.out.print(node.getKey() + " -> ");	// Root
			inorder(node.getRight());				// Right subtree
		}
	}
	
	public void postorder() {
		postorder(root);
	}
	
	private void postorder(BSTNode<T> node) {
		if (node != null) {
			postorder(node.getLeft());				// Left subtree
			postorder(node.getRight());				// Right subtree
			System.out.print(node.getKey() + " -> ");	// Root
		}
	}
	
	public void preorder() {
		preorder(root);
	}
	
	private void preorder(BSTNode<T> node) {
		if (node != null) {
			System.out.print(node.getKey() + " -> ");	// Root
			preorder(node.getLeft());			// Left subtree
			preorder(node.getRight());			// Right subtree
		}
	}
	
	public boolean isEmpty() {
		return (root == null);
	}
	
	// Get smallest element in this BST
	public T min() {
		if (isEmpty())		// If this BST is empty, returns null.
			return null;
		
		else {
			BSTNode<T> node = root;
			while (node.getLeft() != null)
				node = node.getLeft();
			
			return node.getKey();
		}
	}
	
	// Get largest element in this BST
	public T max() {
		if (isEmpty())		// If this BST is empty, returns null.
			return null;
		
		else {
			BSTNode<T> node = root;
			while (node.getRight() != null)
				node = node.getRight();
			
			return node.getKey();
		}
	}

}
