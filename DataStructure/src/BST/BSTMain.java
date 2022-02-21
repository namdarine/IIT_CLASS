package BST;

import Stack.*;

public class BSTMain {
	public static void main (String[] args) throws StackOverflowException, StackUnderflowException {
		BST<Integer> bst = new BST<>();
		
		bst.add(25);
		bst.add(15);
		bst.add(10);
		bst.add(4);
		bst.add(12);
		bst.add(22);
		bst.add(18);
		bst.add(24);
		bst.add(50);
		bst.add(35);
		bst.add(44);
		bst.add(70);
		bst.add(66);
		bst.add(90);
		bst.add(31);
		
		System.out.println("1. Tree's maximum depth: " + bst.maxDepth() + "\n");
		System.out.println("2. Size of the tree with Iterative method: " + bst.iterSize());
		System.out.println("Size of the tree with Recursive method: " + bst.recSize() + "\n");
		System.out.println("3. Traversal of the tree with In-order, pre-order, post-order methods");
		System.out.println("In-order traversal of the tree: ");
		bst.inorder();
		System.out.println("\nPre-order traversal of the tree: ");
		bst.preorder();
		System.out.println("\nPost-order traversal of the tree: ");
		bst.postorder();
		System.out.println("\n4. Smallest number in this tree: " + bst.min());
		
		bst.remove(4);
		bst.remove(50);
		bst.remove(12);
		System.out.println("\nRemove three numbers\n");
		System.out.println("5. Tree's maximum depth: " + bst.maxDepth() + "\n");
		System.out.println("6. Size of the tree with Iterative method: " + bst.iterSize());
		System.out.println("Size of the tree with Recursive method: " + bst.recSize() + "\n");
		System.out.println("7. Traversal of the tree with In-order, pre-order, post-order methods");
		System.out.println("In-order traversal of the tree: ");
		bst.inorder();
		System.out.println("\nPre-order traversal of the tree: ");
		bst.preorder();
		System.out.println("\nPost-order traversal of the tree: ");
		bst.postorder();
		System.out.println("\n8. Smallest number in this tree: " + bst.min());
		System.out.println("\nIs there '35' in this tree? " + bst.contain(35));
		System.out.println("\nIs there '40' in this tree? " + bst.contain(40));
		System.out.println("\n9. Largest number in this tree: " + bst.max());
	}

}
